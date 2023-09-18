from . import views
from django.urls import path
from django.urls.conf import include

urlpatterns = [
     path('', views.test, name="test")
]