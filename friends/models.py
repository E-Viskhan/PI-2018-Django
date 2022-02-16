from django.db import models


class Friend(models.Model):
    first_contact = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE, related_name='first_friends')
    second_contact = models.ForeignKey('contacts.Contact', on_delete=models.CASCADE, related_name='second_friends')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_contact} + {self.second_contact}'

    class Meta:
        unique_together = ('first_contact', 'second_contact')

