from django.contrib import admin
from .models import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated', 'display_order')
    list_editable = ('display_order',)
    list_filter = ('last_updated',)
    search_fields = ('title', 'content')
    ordering = ('display_order',)
    date_hierarchy = 'last_updated'
