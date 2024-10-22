from django.urls import path
from . import views

app_name = 'zodiacWithDB'

urlpatterns = [
    path('', views.zodiac_list, name='zodiac_list'),
    path('<int:sign_id>/', views.zodiac_detail, name='zodiac_detail'),
]
