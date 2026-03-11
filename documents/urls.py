from django.urls import path
from .views import UploadDocument, ListDocuments

urlpatterns = [
    path("upload/", UploadDocument.as_view()),
    path("documents/", ListDocuments.as_view()),
]