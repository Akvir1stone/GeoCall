# Generated by Django 5.0.6 on 2024-06-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevals', '0002_alter_images_image_alter_puser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='new'),
        ),
    ]
