from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        "Data de Criação", auto_now=False, auto_now_add=True
    )
    modified_at = models.DateTimeField(
        "Data de Modificação", auto_now=True, auto_now_add=False
    )

    class Meta:
        abstract = True


class TelegramUser(BaseModel):
    chat_id = models.CharField(
        "Chat ID", max_length=50, blank=False, null=False, unique=True
    )
    first_name = models.CharField("Nome", max_length=100, blank=False, null=True)
    last_name = models.CharField("Sobrenome", max_length=100, blank=False, null=True)

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = "Usuário Telegram"
        verbose_name_plural = "Usuários Telegram"
        ordering = ("created_at",)


class Subscription(BaseModel):
    telegram_user = models.ForeignKey(
        "bot.TelegramUser",
        verbose_name="Telegram User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    manga = models.ForeignKey(
        "mangas.Manga",
        verbose_name="Manga",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        ordering = ("created_at",)
