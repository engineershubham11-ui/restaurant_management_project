from django.http import jsonresponse 
from django.db import detabaseError
from .models import MenuItem

def menu_items_view(request):
    try:
        items = MenuItem.object.all()
        deta = [{"id": item.id, "name": item.name, "price": item.price } for item in items]
        return jsonresponse({"menu_items": data }, status=200)

        except DatabaseError as e:
            return jsonresponse(
                {"error":"we are experiencing database issues. please try again later."},
                status=500
            )
except Exception as e:
    return jsonresponse(
        {"error":"something wenr wrong. please contact support."},
        status=500
    )