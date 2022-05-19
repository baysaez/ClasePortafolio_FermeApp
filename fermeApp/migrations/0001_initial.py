# Generated by Django 4.0.4 on 2022-04-25 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cli', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('p_apellido', models.CharField(max_length=50)),
                ('s_apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('telefono', models.BigIntegerField()),
                ('usuario', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=250)),
                ('pertenencia_emp', models.FloatField(choices=[[0, 'No'], [1, 'Si']])),
                ('tipo_usuario', models.CharField(default='CLIENTE', max_length=30)),
                ('habilitado', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('rut_emp', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('p_apellido', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=50)),
                ('tipo_usuario', models.CharField(max_length=30)),
                ('habilitado', models.FloatField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FamProducto',
            fields=[
                ('id_fam', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'fam_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InvProducto',
            fields=[
                ('id_prod', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('stock_crit', models.IntegerField()),
                ('stock_max', models.IntegerField()),
                ('fecha_venc', models.DateField(blank=True, null=True)),
                ('habilitado', models.FloatField()),
            ],
            options={
                'db_table': 'inv_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfertaProd',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'oferta_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('nro_orden', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'orden_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id_parametro', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('valor', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'parametro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_prov', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
                ('rut', models.CharField(max_length=30)),
                ('rubro', models.CharField(max_length=50)),
                ('celular', models.BigIntegerField()),
                ('domicilio', models.CharField(max_length=220)),
                ('tipo_usuario', models.CharField(max_length=30)),
                ('habilitado', models.FloatField()),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('rut_ven', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('p_apellido', models.CharField(max_length=50)),
                ('s_apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('telefono', models.BigIntegerField()),
                ('usuario', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=250)),
                ('tipo_usuario', models.CharField(max_length=30)),
                ('habilitado', models.FloatField()),
            ],
            options={
                'db_table': 'vendedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaDoc',
            fields=[
                ('nro_doc', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo_venta', models.CharField(max_length=30)),
                ('valor_neto', models.IntegerField()),
                ('iva', models.IntegerField()),
            ],
            options={
                'db_table': 'venta_doc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOferta',
            fields=[
                ('proveedor_id_prov', models.OneToOneField(db_column='proveedor_id_prov', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='fermeApp.proveedor')),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_oferta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('orden_compra_nro_orden', models.OneToOneField(db_column='orden_compra_nro_orden', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='fermeApp.ordencompra')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('observaciones', models.CharField(blank=True, max_length=220, null=True)),
                ('recibido', models.FloatField()),
            ],
            options={
                'db_table': 'detalle_orden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('venta_doc_nro_doc', models.OneToOneField(db_column='venta_doc_nro_doc', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='fermeApp.ventadoc')),
            ],
            options={
                'db_table': 'detalle_venta',
                'managed': False,
            },
        ),
    ]
