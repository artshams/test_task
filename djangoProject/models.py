from django.db import models


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    categories = models.ManyToManyField('Categories', related_name='prods')

    def __str__(self):
        return self.name
