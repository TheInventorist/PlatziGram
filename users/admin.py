from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'phone', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone', 'website', 'picture')
    search_fields = ('user__user_name','user__email', 'user__first_name', 'user__last_name','phone')