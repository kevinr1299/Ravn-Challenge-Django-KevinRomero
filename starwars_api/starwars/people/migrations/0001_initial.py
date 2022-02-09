# Generated by Django 4.0.2 on 2022-02-09 05:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EyeColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HairColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SkinColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('mass', models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('birth_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('eye_color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.eyecolor')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.gender')),
                ('hair_color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.haircolor')),
                ('homeworld', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.world')),
                ('skin_color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='people.skincolor')),
                ('species', models.ManyToManyField(to='people.Specie')),
            ],
        ),
    ]
