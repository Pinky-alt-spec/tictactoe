from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from games.views import MainView, GameJsonListView
from .views import *

urlpatterns = [

    path('', home, name="home"),
    path('play/<room_code>', play, name="play"),

]