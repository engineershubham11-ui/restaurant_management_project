from rest_Framework.decorators import api_view
from rest_Framework.response import Response

@api_view(['GET'])
def get_menu(request):
    menu = [
        {
            "name": "paneer butter masala",
            "description": "delicious cottage cheese in a creamy tomato gravy"
            "price":250
        },
        {
            "name": "chicken biryanni",
            "description": "fragrant bsamati rice coocked with spiced chicken",
            "price":300
        },
        {
            "name": "veg fried rice",
            "description": "stir-fried rice with mixed vegetables and soy sauce",
            "price": 180
        }
    ]
return Response(menu)











