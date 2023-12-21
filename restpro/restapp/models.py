from django.db import models

# Create your models here.


class TestModel(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = 'test'
