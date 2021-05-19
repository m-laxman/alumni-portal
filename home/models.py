from django.db import models
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    query = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
