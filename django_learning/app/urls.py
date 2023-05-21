from django.urls import path
from . import views

# namespace
app_name = 'app'

urlpatterns = [
    path('hello', views.index, name='index'),
]