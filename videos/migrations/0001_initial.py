# Generated by Django 3.2 on 2021-05-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('duration', models.DurationField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('video_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('category', models.ManyToManyField(to='videos.Category')),
                ('membership', models.ManyToManyField(to='membership.Membership')),
            ],
        ),
    ]
