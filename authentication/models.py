from django.db import models
from django.contrib.auth.models import User
import random
import string


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, unique=True)
    balance = models.BigIntegerField(default=0)
    code = models.CharField(max_length=15, unique=True, null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'

    def save(self, *args, **kwargs):
        if not self.code:
            prefix = "LD"
            random_digits = ''.join(random.choices(string.digits, k=10))
            code = prefix + random_digits
            self.code = code
        super().save(*args, **kwargs)


class APIResponse:
    def __init__(self, success, data, message):
        self.success = success
        self.data = data
        self.message = message

    def __dict__(self):
        return {
            'success': self.success,
            'data': self.data,
            'message': self.message
        }
