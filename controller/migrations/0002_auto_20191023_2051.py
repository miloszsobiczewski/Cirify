# Generated by Django 2.2.1 on 2019-10-23 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='que',
            old_name='data',
            new_name='date',
        ),
    ]
