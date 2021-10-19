
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="Tracker"),
    path('productview/<int:prodid>/', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('search/', views.search, name="Search"),

]
