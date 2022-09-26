# Generated by Django 4.1.1 on 2022-09-26 03:35

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
                ('id_cate_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=15)),
                ('nombres', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('celular', models.CharField(max_length=10)),
                ('dni', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('total', models.FloatField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.cliente')),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('precio', models.FloatField()),
                ('imagen', models.CharField(max_length=60)),
                ('cat_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('id_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.orden')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.cliente')),
            ],
        ),
    ]
