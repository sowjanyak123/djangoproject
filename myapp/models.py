from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'blogs/', blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/',blank=True, null=True)

    def __str__(self) -> str:
        return self.title
