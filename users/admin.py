from django.contrib import admin

from users.models import CustomUser, Photos


@admin.register(CustomUser)
class CustomUsersAdmin(admin.ModelAdmin):
    pass


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass
