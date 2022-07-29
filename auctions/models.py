from django.contrib.auth.models import AbstractUser
from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length = 64, blank=False)
    description = models.TextField(blank = False)
    price = models.IntegerField(blank = False)
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

    def __str__(self):
        return f"{self.title}: {self.price}, category: {self.category}"

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listing, blank = True, related_name = "watched")
    listing = models.ForeignKey(Listing, null = True,blank = True, on_delete = models.CASCADE, related_name = "user_listing")

class Bid(models.Model):
    price = models.IntegerField()
    bidder = models.ForeignKey(User, null = False, on_delete = models.CASCADE, related_name = "bidder")
    bid = models.ForeignKey(Listing, null = True, blank = True, related_name = "listing_bid", on_delete=models.CASCADE)

    def __str__(self):
        return f"Bidder: {self.bidder} at ${self.price} for {self.bid}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, null = False, on_delete=models.CASCADE, related_name = "listing")
    description = models.TextField(blank = False)
    commentator = models.ForeignKey(User, null = False, on_delete = models.CASCADE, related_name = "commentator")  