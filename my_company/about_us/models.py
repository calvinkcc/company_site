from django.db import models


class About(models.Model):
    position = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.name
