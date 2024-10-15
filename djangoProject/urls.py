from django.contrib import admin
from django.urls import path, include
from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('calculate.geometry/', include('geometry.urls')),
    path('zodiac/', include('zodiac.urls')),
]
