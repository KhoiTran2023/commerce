# Generated by Django 4.0.5 on 2022-07-26 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lister',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid',
            field=models.ManyToManyField(blank=True, related_name='listing_bid', to='auctions.listing'),
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watched', to='auctions.listing'),
        ),
    ]
