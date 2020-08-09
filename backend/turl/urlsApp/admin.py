from django.contrib import admin
from .models import Entry
# Register your models here.


class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'link', 'path')


admin.site.register(Entry, EntryAdmin)
