from django.db import models


class FetchData(models.Model):

    data = models.CharField(max_length=255)
