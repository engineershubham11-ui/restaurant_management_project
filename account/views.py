#models.py
from django.db import models 

class menu(models.model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digit=6, decimal_places=2)


    def __str__(self):
        return self.name


class order(models.model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=true)
    items = models.ManyToManyField(menu)


    def __str__(self):
        return f"order #{self.id} by {self.customer_name}"


#admin.py

from django.contrib import admin 
from .models import menu, order

@admin.register(menu)
class MenuAdmin(admin.ModeIAdmin):
    list_display = ("name" , "price")
    search_fields = ("name",)

@admin.register(order)
class orderAdmin(admin.modelAdmin):
    list_display = ("id", "customer_name","created_at")
    search_fields = ("customer_name",)
    filter_horizontal = ("items",)













