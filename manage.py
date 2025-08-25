from django import forms

class ContactForm(forms.form):
    name = forms.charfield(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


    def clean_message(Self):
        message = self.cleaned_data.get('message')
        if len(message.strip()) < 10:
            raise forms.validationError("Message should be at least 10 character long.")
    return message


#view.py

from django.shortcuts import render
from .froms import ContactForm

def contact_view(request):
    if request.method == "post":
        form = contactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        print(f"new message from {name} ({email}): {message}")
        return render(request, "contact_success.html")

else:
    form = contactForm()

    return render(request, "contact.html", {"form": form})