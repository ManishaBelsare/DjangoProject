from django.contrib import admin
from ecomapp.models import Menu, contactenquiry

# Register your models here.
class Menu1Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'pdetail', 'is_active']
    list_filter = ['cat', 'is_active']


admin.site.register(Menu, Menu1Admin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(contactenquiry, ContactAdmin)
