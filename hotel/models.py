import datetime
from django.db import models

'''
                                 OCEAN
------------------------------------------------------------------------
| 100 | 102 | 104 | 106 | 108 |ELEV| 110 | 112 | 114 | 116 | 118 | 120 |
------------------------------------------------------------------------
|STAIR|                         HALLWAY                          |STAIR|
------------------------------------------------------------------------
| 101 | 103 | 105 | 107 | 109 |ELEV| 111 | 113 | 115 | 117 | 119 | 121 |
------------------------------------------------------------------------
                               COURTYARD
'''


# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    occupied = models.BooleanField(default=False)

    def oceanside(self):
        return self.room_num % 2 == 0

    def suite(self):
        return self.room_num % 10 <= 1


class Guest(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    vip_num = models.IntegerField(default=-1)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    start = models.DateField(default=datetime.date.today)
    length_of_stay = models.IntegerField(default=1)

    def end(self):
        return self.start + datetime.timedelta(days=self.length_of_stay)
