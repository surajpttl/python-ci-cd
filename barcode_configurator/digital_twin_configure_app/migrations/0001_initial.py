# Generated by Django 4.1.1 on 2022-09-21 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_type', models.CharField(max_length=100)),
                ('value', models.BigIntegerField()),
                ('ts', models.DateTimeField()),
                ('payload', models.JSONField()),
            ],
            options={
                'db_table': 'audit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, primary_key=True, serialize=False)),
                ('code_type', models.CharField(max_length=100)),
                ('code_description', models.CharField(blank=True, max_length=500, null=True)),
                ('pattern_name', models.CharField(blank=True, max_length=250, null=True)),
                ('barcode_type', models.CharField(max_length=250)),
                ('barcode_sample', models.CharField(max_length=250)),
                ('barcode_length', models.IntegerField()),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('part_number', models.CharField(max_length=500)),
                ('part_number_start_at', models.IntegerField(blank=True, null=True)),
                ('part_number_end_at', models.IntegerField(blank=True, null=True)),
                ('vendor_code', models.CharField(max_length=500)),
                ('vendor_code_start_at', models.IntegerField(blank=True, null=True)),
                ('vendor_code_end_at', models.IntegerField(blank=True, null=True)),
                ('batch_code', models.CharField(max_length=500)),
                ('batch_code_start_at', models.IntegerField(blank=True, null=True)),
                ('batch_code_end_at', models.IntegerField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('updated_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'barcode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BusinessUnitMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_business_unit_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'business_unit_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LineMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_line_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('line_type', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'line_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrganizationMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_organization_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=110)),
                ('updated_on', models.DateTimeField()),
            ],
            options={
                'db_table': 'organization_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlantMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_plant_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
                ('dt_business_unit_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='digital_twin_configure_app.businessunitmaster')),
            ],
            options={
                'db_table': 'plant_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StationMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_station_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
                ('dt_line_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='digital_twin_configure_app.linemaster')),
            ],
            options={
                'db_table': 'station_master',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShopMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_shop_id', models.BigIntegerField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('shop_type', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField()),
                ('dt_plant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='digital_twin_configure_app.plantmaster')),
            ],
            options={
                'db_table': 'shop_master',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='linemaster',
            name='dt_shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='digital_twin_configure_app.shopmaster'),
        ),
    ]
