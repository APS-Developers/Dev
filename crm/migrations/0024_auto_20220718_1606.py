# Generated by Django 3.2 on 2022-07-18 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_alter_ticket_changed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalticket',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='changed_by',
        ),
    ]
