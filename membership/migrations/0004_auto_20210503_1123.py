# Generated by Django 3.2 on 2021-05-03 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0002_auto_20210503_1123'),
        ('videos', '0006_auto_20210503_1123'),
        ('membership', '0003_alter_membership_type_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=260)),
                ('stripe_subscription_id', models.CharField(max_length=260)),
                ('cancel_at_end', models.BooleanField(default=False)),
                ('membership', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user_membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='user',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='UserMembership',
        ),
    ]
