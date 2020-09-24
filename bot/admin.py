from django.contrib import admin

from .models import TelegramUser, Subscription


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "first_name", "last_name")
    search_fields = ("chat_id", "first_name", "last_name")


@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ("telegram_user", "manga")
    search_fields = ("first_name", "title")
    list_filter = ("telegram_user",)
