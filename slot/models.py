from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length = 100)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Guest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    #member_since

class Reservation(models.Model):#link with guest
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    date_in = models.DateTimeField()#auto_now_add=True
    date_out = models.DateTimeField()#auto_now_add=True
    made_by = (
        ('E','Email'),
        ('P','Phone Number'),
        ('D','Direct Booking')
        )
    #guest_id =  models.UUIDField(primary_key=True, default=uuid.uuid4)#guest id when it will reference with guest
    guest_id = models.ForeignKey(Guest,on_delete = models.CASCADE)
    choose = models.CharField(
    max_length=1,
    choices=made_by,
    blank=True,
    default='e',
    help_text='Room Status',
    )

class Reserverd_room(models.Model):#link with reservation
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    #Reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room_status = (
        ('e','Empty'),
        ('o','occupied')
    )
    reservation_id = models.ForeignKey(Reservation,on_delete = models.CASCADE)
    status = models.CharField(
    max_length=1,
    choices=room_status,
    blank=True,
    default='e',
    help_text='Room Status',
    )

class Room_type(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    room_id = models.ForeignKey(Room,on_delete = models.CASCADE)
    reserverd_id = models.ForeignKey(Reserverd_room,on_delete = models.CASCADE)

class Occupied_room(models.Model):
    check_in = models.TimeField()
    check_out = models.TimeField()
    reservation_id = models.ForeignKey(Reservation,on_delete = models.CASCADE)
    room_id = models.ForeignKey(Room,on_delete = models.CASCADE)

#every people who stayed in  hotel will have record at hosted_at
class Hosted_at(models.Model):#link with  guest and occupied_room
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #Guest_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #Occupied_room_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    guest_id = models.ForeignKey(Guest,on_delete = models.CASCADE)
    occupied_room_id = models.ForeignKey(Occupied_room,on_delete = models.CASCADE)