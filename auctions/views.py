from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .models import *


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", context = {
        "listings":listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        newListing = Listing(title = request.POST["title"], description = request.POST["description"], price = request.POST["bid"], category = request.POST["category"], img_url = request.POST["imgurl"])
        newListing.save()
        f = Bid(price = request.POST["bid"],bidder = request.user)
        f.save()
        f.bid.add(newListing)
        messages.success(request, "Listing created successfully")
    return render(request, "auctions/create.html")

def categories(request):
    return render(request, "auctions/categories.html")

def category(request, category_id):
    listings = Listing.objects.filter(category = category_id).all()
    return render(request, "auctions/category.html", context = {
        "listings":listings,
    })

def watchlist(request):
    watchedListings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", context = {
        "listings":watchedListings
    })

def watch(request, listing_id):
    f = Listing.objects.get(id = listing_id)
    if f in request.user.watchlist.all():
        request.user.watchlist.remove(f)
        return viewListing(request, listing_id)
    request.user.watchlist.add(f)
    return HttpResponseRedirect(reverse("index"))

def viewListing(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    user = listing.user_listing
    comments = Comment.objects.filter(listing__id=listing_id).all()
    price=Bid.objects.filter(bid__id=listing_id).latest('id')
    return render(request, "auctions/individualListing.html", context = {
        "listing":listing,
        "comments":comments,
        "user_listing":user,
        "price":price,
    })

def comment(request, listing_id):
    if request.method == "POST":
        f = Comment(description = request.POST["comment"], commentator = request.user, listing = Listing.objects.get(id=listing_id))
        f.save()
        return viewListing(request, listing_id)
    return index(request)

def bid(request, listing_id):
    if request.method == "POST":
        if int(request.POST["bid"])<=Bid.objects.filter(bid__id=listing_id).latest('id').price:
            messages.error(request, "Bid amount must be greater than previous bid.")
            return HttpResponseRedirect(reverse("view_listing", kwargs = {'listing_id':listing_id}))
        f = Bid(price = request.POST["bid"], bidder = request.user, bid = Listing.objects.get(id=listing_id))
        f.save()
        return HttpResponseRedirect(reverse("view_listing", kwargs = {'listing_id':listing_id}))