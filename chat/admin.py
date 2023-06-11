from django.contrib import admin

from .models import Message, Room

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
admin.site.register(
    Message,
    MessageAdmin,
)
