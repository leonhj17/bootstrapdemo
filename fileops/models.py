from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UploadFileModel(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()
