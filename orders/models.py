from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
