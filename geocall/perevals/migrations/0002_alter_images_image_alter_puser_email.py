# Generated by Django 5.0.6 on 2024-06-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='puser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
