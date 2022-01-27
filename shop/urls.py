from django.urls import path 
from shop import views
urlpatterns = [
    path("" , views.index ,name = "ShopHome"),
    path("about/" , views.index ,name = "about"),
    path("contacts/" , views.contacts ,name = "contacts"),
    path("tracker/" , views.tracker ,name = "tracker"),
    path("search/" , views.search ,name = "search"),
    path("products/" , views.products ,name = "products"),
    path("checkout/" , views.checkout ,name = "checkout"),

    ]