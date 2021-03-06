# Generated by Django 3.2 on 2021-05-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderlineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.IntegerField(),
        ),
    ]
