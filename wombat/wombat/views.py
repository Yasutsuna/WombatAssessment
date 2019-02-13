# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from wombat.forms import SubmissionForm, UserCreationForm
# from wombat.models import Document
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
# from django.template.defaultfilters import filesizeformat
# from django.core.exceptions import ValidationError
# from .models import Submission
# from wombat.forms import DocumentForm
from django import forms


# @login_required
def home(request):
    return render(request, 'index.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         extra = EmailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# def submission(request):
#         if request.method == 'POST':
#
#             if request.POST.get('book_title') and request.POST.get('description'):
#                 post = Submission()
#                 post.book_title = request.POST.get('book_title')
#                 post.description = request.POST.get('description')
#                 post.save()
#
# #                return render(request, 'upload')
#                 return redirect('upload')
#
#             else:
#                 return render(request, 'submission.html')
#
#         else:
#             return render(request, 'submission.html')


# def upload(request):
#     if request.method == 'POST':
#         form = SubmissionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = SubmissionForm()
#
#     return render(request, 'upload.html', {
#         'form': form
#     })
class UpdateView(SubmissionForm):

    def upload(request):
        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['uploader'] = request.user.id
            form = UpdateView(request.POST, request.FILES)
            form.fields['uploader'].widget = forms.HiddenInput()
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UpdateView()
            form.fields['uploader'].widget = forms.HiddenInput()

        return render(request, 'upload.html', {
            'form': form
        })



# def upload(request):
#     if request.method == 'POST':
#         form = SubmissionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = SubmissionForm()
#
#     return render(request, 'upload.html', {
#         'form': form
#     })


# def list(request):
#     documents = Document.objects.all()
#     return render(request, 'uploadlist.html', { 'documents': documents  })
