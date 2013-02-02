from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=200)
    accept_num = models.IntegerField()
    pub_date = models.DateTimeField('date published')
