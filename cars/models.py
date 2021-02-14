from django.db import models

# Create your models here.

Brand_Choices = (
    ('MERCEDES', 'Mercedes'),
    ('TESLA', 'Tesla'),
    ('BMW', 'bmw'),
    ('AUDI', 'Audi')
)


class Car(models.Model):
    brand = models.CharField(max_length=200, choices=Brand_Choices)
    model = models.CharField(max_length=200)
    max_speed = models.PositiveIntegerField()
    country = models.CharField(max_length=200, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} - {}".format(self.brand, self.model, self.country)

    def save(self, *args, **kwargs):
        if self.brand == 'Tesla':
            self.country = 'USA'
        else:
            self.country = 'Germany'
        super().save(*args, **kwargs)
