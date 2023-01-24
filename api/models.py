from django.db import models
import datetime

# Create your models here.
class Localizacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    urlimagen= models.TextField()
    date = models.DateField(default=datetime.date.today)
    urlmapa= models.TextField()
