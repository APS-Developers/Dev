# Generated by Django 3.2 on 2022-07-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_historicalticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalticket',
            name='history_relation',
        ),
    ]
