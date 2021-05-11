# Generated by Django 3.2.2 on 2021-05-10 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0008_delete_customer'),
        ('checkout', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('order_total', models.IntegerField(default=0)),
                ('grand_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineitem_total', models.IntegerField(default=0)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='membership.membership')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
            ],
        ),
    ]
