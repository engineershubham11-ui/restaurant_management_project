from django.http import HttpResponse
from .models import restaurant 

def mennu_page(request):
    items = menuItem.objects.all()
    return render(request, 'menu.html',{'items': items})
    
    