from django.db import models

# Create your models here.
#backend where to store the product
class Product(models.Model):
    #attributes 
    title       = models.CharField(max_length = 120) # map to database
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=True, null=False) #blank=True means, database not required
    featured    = models.BooleanField() #null=True, default=True