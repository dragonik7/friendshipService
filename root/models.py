import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    friends = models.ManyToManyField('self', through="Friend", through_fields=("from_user", "to_user"))


class Friend(models.Model):
    def __str__(self):
        return f"{self.from_user} to {self.to_user}"
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_id')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_id')

    class Status(models.IntegerChoices):
        SUBMITTED = 1
        REJECTED = 2
        ACCEPTED = 3
        DELETED = 4

    status = models.IntegerField(choices=Status.choices, default=1)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'
        unique_together = ('from_user', 'to_user')
