# Generated by Django 2.0.2 on 2018-02-28 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allobouffe', '0003_remove_restaurant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
