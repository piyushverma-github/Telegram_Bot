from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram_username = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.telegram_username