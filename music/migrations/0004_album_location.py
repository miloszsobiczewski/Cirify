# Generated by Django 2.2.1 on 2019-10-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20191024_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='location',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]