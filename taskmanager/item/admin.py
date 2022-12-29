from django.contrib import admin
from taskmanager.item.models import Item

# class ItemAdmin(admin.ModelAdmin):
#     search_fields = ['id', 'title']
#     list_display = ('id', 'title', 'description', 'created', 'date_to')

admin.site.register(Item)
