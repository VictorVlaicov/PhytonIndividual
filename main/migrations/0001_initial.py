# Generated by Django 4.1.3 on 2022-11-09 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('area', models.FloatField(verbose_name='area')),
                ('floorNumber', models.IntegerField(verbose_name='floorNumber')),
                ('roomCount', models.IntegerField(verbose_name='roomCount')),
                ('price', models.FloatField(verbose_name='price')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, verbose_name='firstName')),
                ('lastName', models.CharField(max_length=30, verbose_name='lastName')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='context')),
                ('datetime', models.DateTimeField(verbose_name='date')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.apartment')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.client')),
            ],
        ),
    ]
