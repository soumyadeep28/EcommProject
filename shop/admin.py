from itertools import product
from django.contrib import admin
from shop import models
# Register your models here.

admin.site.register([
    models.Product
])