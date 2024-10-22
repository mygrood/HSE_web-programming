from django.db import models

class ZodiacSign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='zodiac_images/')

    def __str__(self):
        return self.name
