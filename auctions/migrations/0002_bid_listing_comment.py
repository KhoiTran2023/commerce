# Generated by Django 4.0.5 on 2022-07-25 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(blank=True, choices=[('FAS', 'Fashion'), ('TOY', 'Toys'), ('ELC', 'Electronics'), ('HOM', 'Home'), ('CAR', 'Cars')], max_length=3)),
                ('img_url', models.TextField(blank=True)),
                ('bid', models.ManyToManyField(blank=True, related_name='bid', to='auctions.bid')),
                ('lister', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to=settings.AUTH_USER_MODEL)),
                ('watchlist', models.ManyToManyField(blank=True, related_name='watcher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentator', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='auctions.listing')),
            ],
        ),
    ]