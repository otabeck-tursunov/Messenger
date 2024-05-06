from django.db import models
from userApp.models import *


class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ChatAccount(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
