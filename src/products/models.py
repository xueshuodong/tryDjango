from django.db import models
from django.urls import reverse

# Create your models here.
#backend where to store the product
class Product(models.Model):
    #attributes 
    title       = models.CharField(max_length = 120) # map to database
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=True, null=False) #blank=True means, database not required
    featured    = models.BooleanField(default=False) #null=True, default=True

    # def get_absolute_url(self):
    #     return f"/products/{self.id}/"

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})