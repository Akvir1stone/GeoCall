from django.db import models

# Create your models here.


class PUser(models.Model):
    email = models.EmailField(max_length=50)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


levels = {'lvl1': '1', 'lvl2': '2', 'lvl3': '3', }


class Levels(models.Model):
    winter = models.CharField(choices=levels, null=True, blank=True)
    summer = models.CharField(choices=levels, null=True, blank=True)
    autumn = models.CharField(choices=levels, null=True, blank=True)
    spring = models.CharField(choices=levels, null=True, blank=True)


statuses = {'new': 'Post awaits moderation',
            'pending': 'Post taken for moderation',
            'accepted': 'Post accepted',
            'rejected': 'Post rejected',
            }


class Pereval(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    beauty_title = models.CharField(max_length=30, null=True, blank=True)
    title = models.CharField(max_length=60)
    other_titles = models.CharField(max_length=60, null=True, blank=True)
    connect = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(PUser, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE, null=True, blank=True)
    levels = models.ForeignKey(Levels, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(choices=statuses)


class Images(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=250)
    per = models.ForeignKey(Pereval, on_delete=models.CASCADE)
