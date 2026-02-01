from django.contrib import admin
from .models import User, Housing


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone')
    search_fields = ('full_name', 'phone')


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'user')
    search_fields = (
        'location',
        'description',
        'user__full_name',
        'user__phone'
    )
    list_filter = ('location',)


