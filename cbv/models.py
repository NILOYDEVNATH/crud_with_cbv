from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    status=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)