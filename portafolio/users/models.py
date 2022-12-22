from django.db import models

from django.db import models

# Create your models here.
class Ips(models.Model):
    ip = models.CharField(max_length=200)
