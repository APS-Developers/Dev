# Generated by Django 3.2 on 2022-07-05 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_orgid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='OrgID',
        ),
    ]
