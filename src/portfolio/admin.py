from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'url')
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)
