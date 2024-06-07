from django.db import models

# Create your models here.


class PUser(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


levels = {'lvl1': '1', 'lvl2': '2', 'lvl3': '3', }


class Levels(models.Model):
    winter = models.CharField(choices=levels)
    summer = models.CharField(choices=levels)
    autumn = models.CharField(choices=levels)
    spring = models.CharField(choices=levels)


class Pereval(models.Model):
    date_added = models.DateTimeField()


class Images(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=250)
    per = models.ForeignKey(Pereval, on_delete=models.CASCADE)
