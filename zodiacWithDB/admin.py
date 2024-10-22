from django.contrib import admin
from .models import ZodiacSign

@admin.register(ZodiacSign)
class ZodiacSignAdmin(admin.ModelAdmin):
    list_display = ('name',)
