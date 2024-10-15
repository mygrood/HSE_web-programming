from django.urls import path
from .views import show_all_signs, show_sign

app_name = 'zodiac'
urlpatterns = [
    path('all/', show_all_signs, name='show_all_signs'),
    path('<str:sign_name>/', show_sign, name='show_sign'),
]
