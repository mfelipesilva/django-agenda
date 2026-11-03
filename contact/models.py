from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # blank true faz com que o campo seja opcional
    email = models.EmailField( max_length=254, blank=True) 
    # ↓ isso faz com que o registro de data e hora seja executado na hora que o usuário for criado, dinamicamente
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()