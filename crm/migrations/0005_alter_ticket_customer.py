# Generated by Django 3.2 on 2022-07-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20220630_1331'),
        ('crm', '0004_auto_20220702_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer'),
        ),
    ]