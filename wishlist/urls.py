from django.urls import path
from wishlist import views

urlpatterns = [
    path('', views.show, name="show"),

]