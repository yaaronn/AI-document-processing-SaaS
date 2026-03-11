from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):

    list_display = ("id", "file", "status", "created_at")

    readonly_fields = ("extracted_text",)


admin.site.register(Document, DocumentAdmin)