from django.db import models


class Links(models.Model):
    url = models.URLField()
    url_shortener = models.CharField(max_length=8, unique=True)
# DATE - adicionar metodo de expiração do link data/hora


def __str__(self) -> str:
    return self.url_shortener
