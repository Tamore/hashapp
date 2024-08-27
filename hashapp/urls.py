from django.urls import path
from hashapp import views

urlpatterns = [
    path('', views.index),
    path('setting', views.setting),
    path('upload', views.upload),
    path('follow', views.follow),
    path('search', views.search),
    path('profile/<pk>', views.profile),
    path('likes', views.likes),
    path('signup', views.signup),
    path('signin', views.signin),
    path('logout', views.logout),
]