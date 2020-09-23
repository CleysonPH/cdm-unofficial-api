from django.contrib import admin

from .models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "first_name", "last_name")
    search_fields = ("chat_id", "first_name", "last_name")
