from celery import shared_task
from .models import Document
from .ocr import extract_text_from_image
from .ai_extract import extract_invoice_data


@shared_task
def process_document(document_id):

    document = Document.objects.get(id=document_id)

    document.status = "processing"
    document.save()

    try:

        text = extract_text_from_image(document.file.path)

        document.extracted_text = text

        print("OCR TEXT:", text)

        data = extract_invoice_data(text)

        print("AI DATA:", data)

        document.extracted_data = data

        document.status = "completed"

        document.save()

    except Exception as e:

        print("AI ERROR:", e)

        document.status = "failed"
        document.save()