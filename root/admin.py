from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from root.models import Friend, User


admin.site.register(User, UserAdmin)

# Register your models here.

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('from_user_id', 'to_user_id', 'status', 'created_at')
    readonly_fields = ['created_at']
    list_display_links = ['status']
