from django.db import models


# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    enterprise = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    suite_number = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'User'
