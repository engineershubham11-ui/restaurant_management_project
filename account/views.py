from django.shortcuts import render
from .models import menuitem

def homepage(request):
    query = request.GET.get('q')
    if query:
        items = menuitem.object.filter(name__icontains=query)
        else:
            items = menuitem.object.all()

        return render(request, 'homepage.html',{'items': items, 'query': query})
        