from django.db import models 

class Feedback(models.model):
    comment = models.TextField ()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F"feedback #{self.id} -{self.submitted_at"}





forms.py


from django import forms
form.models import Feedback

class FeedbackForm(forms.modelsForm):
    class meta:
        model = Feedback
        fields = ['comment']






views.py

form django.shortcuts import render, redirect
from.form import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = feedbackform(request.post)
        if form.is_valid():
            form.save()
            return redirect('feedback')
        else:
            form = feedbackform()
            return render(request, "feedback.html" , {"form":form})





urls.py

from django.urls import path 
from . import views

urlpattern = [
    path('feedback/', views.feedback_view, name='feedback'),
]




