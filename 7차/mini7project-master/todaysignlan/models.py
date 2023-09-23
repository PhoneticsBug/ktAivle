from django.db import models

class Sign(models.Model):
    image = models.ImageField(upload_to='signoftheday/')
    description = models.TextField()
    name = models.CharField(max_length=200)
