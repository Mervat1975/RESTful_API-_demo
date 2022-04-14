
from django.utils import timezone
from django.db import models


class Student(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    amount_due = models.FloatField()
    dob = models.DateField(blank=True, null=True, default=None)
