from django.db import models


# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    file_count = models.IntegerField(default=0)

    def __str__(self):
        return "{name}({size}) {path}".format(
            name=self.name, path=self.path, size=self.file_count)


class ImageModel(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    size = models.IntegerField(default=0)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return "{name}({size}) {path}".format(
            name=self.name, path=self.path, size=self.size)