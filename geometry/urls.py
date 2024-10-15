from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='rectangle_area'),
    path('square/<int:width>/', views.get_square_area, name='square_area'),
    path('circle/<int:radius>/', views.get_circle_area, name='circle_area'),
]