from django.urls import path
from store import views


urlpatterns = [
    path('', views.index, name="index"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('login/', views.login, name="login"),
    path('login/check/', views.check, name="check"),
    path('login/signup/', views.signup, name="signup"),
    path('login/signup/addmember/', views.addmember, name="addmember"),
    path('wishlist/addToList/', views.addToList, name="addtolist"),
    path('wishlist/home/', views.redirect, name="redirect"),
]