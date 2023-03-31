from django.db import models

# Create your models here.
class cadatro(models.Model):
    nome = models.Field.verbose_name("nome",  max_length=30)
    