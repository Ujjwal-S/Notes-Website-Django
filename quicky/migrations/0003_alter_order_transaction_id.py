# Generated by Django 3.2.4 on 2021-07-04 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quicky', '0002_rename_note_orderitem_note_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
