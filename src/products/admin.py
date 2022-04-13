from django.contrib import admin
from .models import Product #relative import(because admin and models are in the same directory, module), importing Product class from models.py
# Register your models here.

admin.site.register(Product)
