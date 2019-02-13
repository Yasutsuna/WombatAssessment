from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.contrib import admin
from django.db.models import FileField
import os


from django.shortcuts import render, redirect


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160


#def int_from_bytes(x):
#    return x.to_bytes((x.bit_length() + 7) // 8, 'big')



def validate_file_size(value):
    extension = ['.pdf', '.doc', '.docx']
    fileextension=os.path.splitext(value.name)[1]

    if value.size > 104857600:
        # Upload limit problem on heroku side.
        raise ValidationError("File is too big")
    if not fileextension.lower() in extension:
        raise ValidationError("File must be in PDF or docx format")
    else:
        return value


class Submission(models.Model):
    PENDING = 'PE'
    ACCEPTED = 'AC'
    REJECTED = 'RE'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )

    book_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    document = models.FileField(upload_to='', validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    book_status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    uploader = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.book_title




# class Document(models.Model):
#
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='', validators=[validate_file_size])
#     uploaded_at = models.DateTimeField(auto_now_add=True)



