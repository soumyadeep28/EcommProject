from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    list_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.product_name