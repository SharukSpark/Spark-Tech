# Generated by Django 5.1 on 2024-09-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sparktechapp', '0002_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
