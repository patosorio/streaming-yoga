# Generated by Django 3.2 on 2021-05-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='stripe_plan_id',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='stripe_subscription_id',
        ),
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
