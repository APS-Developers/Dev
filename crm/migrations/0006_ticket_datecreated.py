# Generated by Django 3.2 on 2022-07-03 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_ticket_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='DateCreated',
            field=models.DateField(default=datetime.date(2022, 7, 3), verbose_name='Date Created'),
        ),
    ]