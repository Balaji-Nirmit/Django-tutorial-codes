# Generated by Django 5.0.2 on 2024-02-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='uploaded_images'),
        ),
    ]
