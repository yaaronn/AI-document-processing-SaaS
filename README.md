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

User Upload → Django API → Redis Queue → Celery Worker → OCR → LLM → Structured Data → Database
