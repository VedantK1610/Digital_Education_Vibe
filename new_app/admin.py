from django.contrib import admin

from new_app.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','course','phone_number','message')

admin.site.register(Contact,ContactAdmin)