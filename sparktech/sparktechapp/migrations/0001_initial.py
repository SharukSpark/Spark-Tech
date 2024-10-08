# Generated by Django 5.1 on 2024-09-01 02:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='coolingsystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Product_Dimensions', models.TextField()),
                ('Brand', models.TextField()),
                ('Power_Connector_Type', models.TextField()),
                ('Voltage', models.TextField()),
                ('Cooling_Method', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, 'Liquid Cooler-360mm'), (2, 'Liquid Cooler-240mm'), (3, 'Liquid Cooler-120mm'), (4, 'Custom-RGB CPU Cooler'), (5, 'CPU-RGB Cooler')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='graphiccard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Graphics_Coprocessor', models.TextField()),
                ('Brand', models.TextField()),
                ('RAM_Size', models.TextField()),
                ('GPU_Clock_Speed', models.TextField()),
                ('Manufacturer', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, '4060 Series'), (2, '3050 Series'), (3, '1650 Series')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='harddrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Digital_Storage_Capacity', models.TextField()),
                ('Hard_Disk_Interface', models.TextField()),
                ('Connectivity_Technology', models.TextField()),
                ('Brand', models.TextField()),
                ('Hard_Disk_Form_Factor', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, '256GB'), (2, '500GB'), (3, '1TB'), (4, '2TB'), (5, ' 4TB')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Brand', models.TextField()),
                ('CPU_Socket', models.TextField()),
                ('Compatible_Devicesl', models.TextField()),
                ('RAM_Memory', models.TextField()),
                ('Compatible_Processors', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, 'DDR 5'), (2, 'ThreadRipper Series'), (3, '650 Series'), (4, '550 Series'), (5, '450 Series')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Brand', models.TextField()),
                ('CPU_Manufacture', models.CharField(max_length=255)),
                ('CPU_Model', models.TextField()),
                ('CPU_Speed', models.TextField()),
                ('CPU_Socket', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, 'ryzen3'), (2, 'ryzen5'), (3, 'ryzen7'), (4, 'ryzen9'), (5, 'Threadripper'), (6, 'i3'), (7, 'i5'), (8, 'i7'), (9, 'i9')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Computer_Memory_Size', models.TextField()),
                ('Brand', models.TextField()),
                ('RAM_Memory_Technology', models.TextField()),
                ('Memory_Speed', models.TextField()),
                ('Compatible_Devices', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, '8GB'), (2, '16GB'), (3, '32GB'), (4, '64GB')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='smbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Model_Name', models.TextField()),
                ('Brand', models.TextField()),
                ('Connector_Type', models.TextField()),
                ('Output_Wattage', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, '400W'), (2, '500W'), (3, '600W'), (4, '800W'), (5, '1000W')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='ssd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Digital_Storage_Capacity', models.TextField()),
                ('Hard_Disk_Interface', models.TextField()),
                ('Connectivity_Technology', models.TextField()),
                ('Brand', models.TextField()),
                ('Hard_Disk_Form_Factor', models.TextField()),
                ('About_item1', models.TextField()),
                ('About_item2', models.TextField()),
                ('card_name', models.TextField()),
                ('img1', models.ImageField(upload_to='image')),
                ('img2', models.ImageField(upload_to='image')),
                ('card_img', models.ImageField(upload_to='image')),
                ('cat', models.IntegerField(choices=[(1, '256GB'), (2, '500GB'), (3, 'M.2 NVMe 256GB'), (4, 'M.2 NVMe 500GB'), (5, 'M.2 NVMe 1TB')], verbose_name='category')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sparktechapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='CART',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('uid', models.ForeignKey(db_column='userid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Coolingsystem', models.ForeignKey(blank=True, db_column='coolingsystem', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.coolingsystem')),
                ('Graphiccard', models.ForeignKey(blank=True, db_column='graphiccard', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.graphiccard')),
                ('Motherboard', models.ForeignKey(blank=True, db_column='motherboard', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.motherboard')),
                ('Processor', models.ForeignKey(blank=True, db_column='processor', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.processor')),
                ('Ram', models.ForeignKey(blank=True, db_column='ram', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.ram')),
                ('Smbs', models.ForeignKey(blank=True, db_column='smbs', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.smbs')),
                ('Ssd', models.ForeignKey(blank=True, db_column='ssd', null=True, on_delete=django.db.models.deletion.CASCADE, to='sparktechapp.ssd')),
            ],
        ),
    ]
