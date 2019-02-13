from django.contrib import admin
from .models import Submission
from . import models


class SubmissionAdmin(admin.ModelAdmin):
    model = models.Submission
    list_display = ('book_title', 'book_status', 'description', 'document', 'uploaded_at', 'uploader')
    list_filter = (
        ('book_status'),
    )


admin.site.register(Submission, SubmissionAdmin)
