from django.db import models


class Profile(models.Model):
    status = models.ForeignKey('users.CustomUser', to_field='status', related_name='status')

    class Meta:
        fields = '__all__'

