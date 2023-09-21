from django.contrib import admin
from .models import PersonalInfo, Section


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')

    def has_add_permission(self, request):
        return not bool(PersonalInfo.objects.count())

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("page", "title", "last_updated", "display_order")
    list_editable = ("display_order",)
    list_filter = ("page", "last_updated",)
    search_fields = ("title", "content")
    ordering = ("display_order",)
    date_hierarchy = "last_updated"
