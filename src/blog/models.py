from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    body  = models.TextField(blank=False)

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})
