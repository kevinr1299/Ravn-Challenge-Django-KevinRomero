# Generated by Django 4.0.2 on 2022-02-12 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_alter_eyecolor_name_alter_gender_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='species',
        ),
        migrations.AddField(
            model_name='person',
            name='species',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='people.specie'),
            preserve_default=False,
        ),
    ]