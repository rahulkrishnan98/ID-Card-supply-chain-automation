# Generated by Django 2.1.5 on 2019-04-28 05:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0017_auto_20190428_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
