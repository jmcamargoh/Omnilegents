# Generated by Django 4.1.3 on 2023-02-22 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_Usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('domicilio', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
