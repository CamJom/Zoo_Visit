from django.db import models

# Create your models here.


class SubUser(models.Model):
    name = models.CharField(max_length=50, default="")
    favoriteAnimal = models.CharField(max_length=50, default="")
    favoriteColor = models.CharField(max_length=50, default="")

    animal = models.ManyToManyField(
        "animals.Animal",
        related_name="aminals",
        blank=True
    )

    def __str__(self):
        return f"{self.name}"
