# Generated by Django 4.0.5 on 2022-07-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_user_listing_user_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watched', to='auctions.listing'),
        ),
    ]
