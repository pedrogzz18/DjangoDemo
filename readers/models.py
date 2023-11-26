from django.db import models
from ourbooks.models import Reader, Editorial
import datetime

class Ownership(models.Model):
    reader = models.ForeignKey(to=Reader, on_delete=models.CASCADE)
    editorial = models.ForeignKey(to=Editorial, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=True)
    shared = models.BooleanField(default=False)
    acquisition_date = models.DateField()
