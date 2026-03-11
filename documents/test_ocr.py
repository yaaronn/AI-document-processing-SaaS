from documents.ocr import extract_text_from_image

text = extract_text_from_image("documents/sample_invoice.png")
print(text)