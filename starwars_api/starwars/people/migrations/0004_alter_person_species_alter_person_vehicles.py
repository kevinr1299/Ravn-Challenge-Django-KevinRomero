# Generated by Django 4.0.2 on 2022-02-10 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('people', '0003_alter_person_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='species',
            field=models.ManyToManyField(null=True, to='people.Specie'),
        ),
        migrations.AlterField(
            model_name='person',
            name='vehicles',
            field=models.ManyToManyField(null=True, to='vehicles.Vehicle'),
        ),
    ]