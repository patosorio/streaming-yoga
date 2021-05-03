# Generated by Django 3.2 on 2021-05-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_auto_20210503_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='user_membership',
        ),
    ]
