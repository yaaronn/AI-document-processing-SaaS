# AI Document Processing SaaS

An AI-powered backend system that extracts structured data from documents using OCR and LLMs.

## Features

- Upload documents via REST API
- OCR extraction using Tesseract
- AI data extraction using OpenRouter
- Asynchronous processing using Celery
- Redis task queue
- Django REST Framework backend

## Tech Stack

- Python
- Django
- Django REST Framework
- Celery
- Redis
- Tesseract OCR
- OpenRouter LLMs

## System Architecture
          +-------------+
          |   Client    |
          +-------------+
                 |
                 v
        +----------------+
        |   Django API   |
        +----------------+
                 |
                 v
           +-----------+
           |   Redis   |
           +-----------+
                 |
                 v
         +----------------+
         | Celery Worker  |
         +----------------+
           |          |
           v          v
       OCR Engine     LLM (OpenRouter)
           |
           v
        Database

API examples
## API Endpoints

### Upload Document

POST /api/upload

Example request:

curl -X POST -F "file=@invoice.png" http://localhost:8000/api/upload/

Example response:

{
  "id": 1,
  "status": "uploaded"
}
OUTPUT examples
### Extracted Data

{
  "invoice_number": "INV-102",
  "vendor": "ABC Company",
  "total_amount": 320
}



User Upload → Django API → Redis Queue → Celery Worker → OCR → LLM → Structured Data → Database
