from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'status', 'rating', 'owner', 'created_at')
    list_filter = ('status', 'genre')
    search_fields = ('title', 'genre')
