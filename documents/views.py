from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Document
from .serializers import DocumentSerializer
from .ocr import extract_text_from_image
from .ai_extract import extract_invoice_data
from .tasks import process_document


class UploadDocument(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):

        serializer = DocumentSerializer(data=request.data)

        if serializer.is_valid():

            document = serializer.save()

            process_document.delay(document.id)
            return Response(DocumentSerializer(document).data)

            try:
                text = extract_text_from_image(document.file.path)

                document.extracted_text = text
                data = extract_invoice_data(text)
                document.extracted_data = data
                document.status = "completed"
                document.save()

            except Exception as e:

                document.status = "failed"
                document.save()

            return Response(DocumentSerializer(document).data)

        return Response(serializer.errors)

class ListDocuments(APIView):

    def get(self, request):

        documents = Document.objects.all()

        serializer = DocumentSerializer(documents, many=True)

        return Response(serializer.data)    