from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Bid(models.Model):
    price = models.IntegerField()
    bidder = models.ForeignKey(User, null = False, on_delete = models.CASCADE, related_name = "bidder")

class Listing(models.Model):
    title = models.CharField(max_length = 64, blank=False)
    description = models.TextField(blank = False)
    price = models.IntegerField(blank = False)
    bid = models.ManyToManyField(Bid, blank = True, related_name = "bid")
    category_choices = [
        ('NON', ''),
        ('FAS', 'Fashion'),
        ('TOY', 'Toys'),
        ('ELC', 'Electronics'),
        ('HOM', 'Home'),
        ('CAR', 'Cars')
    ]
    category = models.CharField(max_length=3, choices = category_choices, blank = True)
    img_url = models.TextField(blank = True)
    lister = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "listing")
    watchlist = models.ManyToManyField(User, blank = True, related_name = "watcher")

class Comment(models.Model):
    listing = models.ForeignKey(Listing, null = False, on_delete=models.CASCADE, related_name = "listing")
    description = models.TextField(blank = False)
    commentator = models.ForeignKey(User, null = False, on_delete = models.CASCADE, related_name = "commentator")