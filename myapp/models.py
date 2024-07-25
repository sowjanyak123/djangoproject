from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'blogs/', blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

