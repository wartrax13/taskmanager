from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created = models.DateField(default=timezone.now(), editable=True)
    date_to = models.DateField(null=True, blank=True) 
