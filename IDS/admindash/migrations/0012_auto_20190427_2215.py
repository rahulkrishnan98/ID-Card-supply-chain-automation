# Generated by Django 2.1.5 on 2019-04-27 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0011_auto_20190427_2214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientdetail',
            old_name='phone',
            new_name='phonenum',
        ),
    ]
