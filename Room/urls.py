from django.urls.conf import path
from rest_framework import routers, urlpatterns
from django.urls import path, include
from . import views

router=routers.DefaultRouter()

router.register('Rooms',viewset=views.AllRooms,basename='room')

urlpatterns=[
    path('',include(router.urls))
]