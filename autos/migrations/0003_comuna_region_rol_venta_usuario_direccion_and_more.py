# Generated by Django 4.2.1 on 2024-06-29 00:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idCom', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del rol')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del usuario')),
                ('rut', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('fNacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=12)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autos.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=6)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autos.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autos.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='autos.region'),
        ),
    ]
