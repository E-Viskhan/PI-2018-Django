from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True);
