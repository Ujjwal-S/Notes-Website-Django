# Generated by Django 3.2.4 on 2021-06-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
