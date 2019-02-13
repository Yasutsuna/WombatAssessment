from django import forms
# from wombat.models import Document
from wombat.models import Submission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
# #        fields = ('description', 'document', )
#         fields = ( 'document', )
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", )


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('book_title', 'description', 'document', 'uploader')
