# Generated by Django 4.2 on 2023-06-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albom',
            name='sana',
            field=models.DateField(blank=True, null=True),
        ),
    ]
