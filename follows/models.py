from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='followed')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')

