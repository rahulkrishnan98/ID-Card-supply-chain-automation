# Generated by Django 2.1.5 on 2019-04-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0020_uploadtemplate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadtemplate',
            old_name='image',
            new_name='bimage',
        ),
        migrations.AddField(
            model_name='uploadtemplate',
            name='fimage',
            field=models.ImageField(default='static/template/main.jpg', upload_to='static/template/'),
        ),
    ]
