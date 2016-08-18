from django.contrib import admin
from app.models import Node


class NodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'father_id')

admin.site.register(Node, NodeAdmin)
# Register your models here.
