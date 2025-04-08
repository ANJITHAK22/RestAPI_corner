
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('user/',views.get_user,name='get_user'),
    path('user/create',views.create_user,name='create_user'),
#     path('user/<int:pk>',views.updation_user,name='updation_user')
 ]
