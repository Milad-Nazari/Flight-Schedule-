# Generated by Django 3.2.8 on 2021-11-09 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0007_auto_20211102_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='Flight_Date',
            field=models.DateTimeField(),
        ),
    ]
