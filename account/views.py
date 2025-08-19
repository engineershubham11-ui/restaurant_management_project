#models.py
from django.db import models 
from django.contrib.auth.models import user

class menu(models.model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digit=6, decimal_places=2)


    def __str__(self):
        return self.name


class order(models.model):
    STATUS_CHOICES =[
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed')
        ('CANCELLED', 'cancelled')
    ]

    customer = Models.ForeignKey(user, on_delete=models.CASCADE, RELATED_name="orders")
    item = models.ManyToManyField(menu, related_name="orders")
    total_amount = model.DecimalField(max_length=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"order #{self.id} by {self.customer.username} -{self.status}"


#admin.py

from django.contrib import admin 
from .models import menu, order

@admin.register(menu)
class MenuAdmin(admin.ModeIAdmin):
    list_display = ("name" , "price")
    search_fields = ("name",)

@admin.register(order)
class orderAdmin(admin.modelAdmin):
    list_display = ("id", "customer","total_amount", "status", "created_at")
    search_fields = ("customer_name",)
    filter_horizontal = ("items",)













