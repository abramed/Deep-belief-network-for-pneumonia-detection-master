import os
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Image(models.Model):
	image=models.ImageField(upload_to='media/')
