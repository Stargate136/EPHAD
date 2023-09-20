from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'sent_at', 'is_processed', 'processed_at')
    list_filter = ('is_processed', 'sent_at', 'processed_at')
    search_fields = ('email', 'subject')
    ordering = ('-sent_at',)

    readonly_fields = ('email', 'subject', 'message', 'sent_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
