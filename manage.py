from django.urls import path
from . import views

urlpattern = [
    path('',views.home, name='home'),
    path('faq/', views.faq, name='faq'),
]

#views.py
from django.shortcuts import render

def home(request);
  return render(request, 'home.html')

  def faq(request):
    faq = [
        {"questiion":"what is the purpose of these site?","answer": "this site provide information about our services."},
        {"questions": "how can i contact support?", "answer":"you can reach us via the contact page or email support@example.com"},
        {"questions":"do you offer refaunds?", "answer": "yes, refaund are processed within 7 working days"},
    ]

return render (request, 'faq.html', {'faqs': faqs})
