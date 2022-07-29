from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name = "create"),
    path("categories", views.categories, name = "categories"),
    path("category/<str:category_id>", views.category, name = "category"),
    path("watchlist", views.watchlist, name = "watchlist"),
    path("view/<int:listing_id>", views.viewListing, name = "view_listing"),
    path("watch/<int:listing_id>", views.watch, name = "watch"),
    path("comment/<int:listing_id>", views.comment, name = "comment"),
    path("bid/<int:listing_id>", views.bid, name = "bid"),
]
