# Generated by Django 3.2 on 2022-07-02 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_auto_20220630_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('TicketID', models.AutoField(primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=100)),
                ('SubCategory', models.CharField(max_length=100, verbose_name='Sub-Category')),
                ('ModelNo', models.CharField(max_length=100, verbose_name='Model No')),
                ('SerialNo', models.CharField(max_length=100, verbose_name='Serial No')),
                ('Summary', models.TextField(blank=True, max_length=500)),
                ('Priority', models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4')], max_length=2)),
                ('AMC', models.BooleanField()),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Resolved', 'Resolved'), ('Pending', 'Pending'), ('Closed', 'Closed')], max_length=10)),
                ('FaultFoundCode', models.CharField(choices=[('Router', 'Router faulty'), ('Modem', 'Modem faulty'), ('Switch', 'Switch faulty')], max_length=30, verbose_name='Fault Found Code')),
                ('ResolutionCode', models.CharField(choices=[('123', 'Router faulty'), ('456', 'Modem faulty')], max_length=20, verbose_name='Resolution Code')),
                ('ResolutionRemarks', models.TextField(blank=True, max_length=500, verbose_name='Resolution Remarks')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
            ],
            options={
                'db_table': 'Ticket',
            },
        ),
    ]