# Generated by Django 3.2.5 on 2021-07-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicky', '0003_alter_order_transaction_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='transaction_id',
            new_name='recipt',
        ),
        migrations.AddField(
            model_name='order',
            name='r_order_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
