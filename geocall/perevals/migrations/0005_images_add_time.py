# Generated by Django 5.0.6 on 2024-06-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevals', '0004_alter_levels_autumn_alter_levels_spring_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-01 01:01'),
            preserve_default=False,
        ),
    ]
