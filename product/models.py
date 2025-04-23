from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField() #Ensures stock is not negative

    def __str__(self):
        return f"{self.name} -- Quantity:{self.stock}"

#pass - abdultheone