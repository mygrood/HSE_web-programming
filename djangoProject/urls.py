from django.contrib import admin
from django.urls import path, include
from djangoProject import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('calculate.geometry/', include('geometry.urls')),
    path('zodiac/', include('zodiac.urls')),
    path('zodiac_db/', include('zodiacWithDB.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)