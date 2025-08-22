EMAIL_BACKEND = 'django.core.mail.backends.smtp.emailbackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS =True
EMAIL_USE_TLS = 'YOUR_EMAIL@GAMIL.COM'
EMAIL_HOST_PASSWORD = 'your_email_password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER






 django.db import models

class contactform(forms.form):
    name = forms.charField(max_length=100)
    email  = forms.emailfield()
    message = forms.charfield(width=forms.Textarea)    
    