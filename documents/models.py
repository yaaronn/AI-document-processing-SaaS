from django.db import models


class Document(models.Model):

    STATUS_CHOICES = [
        ("uploaded","uploaded"),
        ("processing","processing"),
        ("completed","completed"),
        ("failed","failed")
    ]

    file = models.FileField(upload_to="documents/")

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="uploaded"
    )

    extracted_text = models.TextField(null=True, blank=True)

    extracted_data = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name