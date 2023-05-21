from django.urls import path
from . import views

# namespace
app_name = 'app'

urlpatterns = [
    path('hello', views.index, name='index'),
    path('page/<str:user_name>', views.user_page, name='user_name'),
    path('number_page/<str:user_name>/<int:number>', views.number_page, name='number_page'),

]