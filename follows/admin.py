from django.contrib import admin

from follows.models import Follow


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    pass

