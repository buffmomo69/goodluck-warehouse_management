# Generated by Django 4.1 on 2022-09-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invenotry', '0002_vehicle_marka_receiveddate_stocksentdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stocksentdetail',
            name='markname',
        ),
        migrations.RemoveField(
            model_name='stocksentdetail',
            name='total',
        ),
        migrations.AddField(
            model_name='stocksentdetail',
            name='markname',
            field=models.ManyToManyField(related_name='stocksentdetail_markname', to='invenotry.marka', verbose_name='Marka'),
        ),
        migrations.AddField(
            model_name='stocksentdetail',
            name='total',
            field=models.ManyToManyField(related_name='stocksentdetail_total', to='invenotry.marka', verbose_name='Total Cartoon'),
        ),
    ]