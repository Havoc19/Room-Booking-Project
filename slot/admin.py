from django.contrib import admin
from .models import Room,Guest,Reservation,Reserverd_room,Room_type,Occupied_room,Hosted_at
# Register your models here.
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Reserverd_room)
admin.site.register(Room_type)
admin.site.register(Occupied_room)
admin.site.register(Hosted_at)