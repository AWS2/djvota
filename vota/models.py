from django.db import models

# Create your models here.

class Votacio(models.Model):
	titol = models.CharField(max_length=255)
	desc = models.TextField(blank=True,null=True)

class Opcio(models.Model):
	titol = models.CharField(max_length=255)
	desc = models.TextField(blank=True,null=True)
	votacio = models.ForeignKey(Votacio, on_delete=models.CASCADE)


