from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(blank=True, null=True, default='myapp/img/default.jpg')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = "myapp/img/default.jpg"
        super().save(*args, **kwargs)