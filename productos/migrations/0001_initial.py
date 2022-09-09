# Generated by Django 4.1 on 2022-09-09 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('id_domicilio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.domicilio')),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=70)),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
                ('cat_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.orden')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.usuario'),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.usuario'),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.usuario')),
            ],
        ),
    ]
