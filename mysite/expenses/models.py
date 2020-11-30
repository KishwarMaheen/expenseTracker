from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    total_amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
