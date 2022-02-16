from django.contrib import admin
from contacts.models import Contact, Address


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass