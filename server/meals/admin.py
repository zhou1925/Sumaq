from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created']
    list_filter = ['name', 'price']
