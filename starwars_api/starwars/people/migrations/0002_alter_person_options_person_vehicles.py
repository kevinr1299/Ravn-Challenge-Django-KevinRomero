# Generated by Django 4.0.2 on 2022-02-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.AddField(
            model_name='person',
            name='vehicles',
            field=models.ManyToManyField(to='vehicles.Vehicle'),
        ),
    ]