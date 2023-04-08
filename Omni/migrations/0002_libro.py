# Generated by Django 4.1.6 on 2023-03-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Omni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('bookID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=120)),
                ('autores', models.CharField(max_length=250)),
                ('isbn13', models.CharField(max_length=14)),
                ('num_pages', models.IntegerField()),
                ('fecha_publicacion', models.DateField()),
                ('editorial', models.CharField(max_length=50)),
            ],
        ),
    ]