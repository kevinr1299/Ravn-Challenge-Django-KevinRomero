# Generated by Django 4.0.2 on 2022-02-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]