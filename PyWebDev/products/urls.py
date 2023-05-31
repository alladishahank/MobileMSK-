from django.urls import path
from . import views

urlpatterns = [
    # root of app
    path('', views.index),
    # products page
    path('new',views.new)
]
