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
BASE_PRICE = 135.00
OCEANSIDE_SURCHARGE = 100.00
SUITE_SURCHARGE = 75.00
MAXIMUM_STAY = 7  # makes occupied queries easier


# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(default=0)
    occupied = models.BooleanField(default=False)

    def oceanside(self):
        return self.room_num % 2 == 0

    def suite(self):
        return (self.room_num % 10) <= 1

    '''
    def occupied(self, date):
        # there may be a better way to do this...
        bookings = self.booking_set.filter(end__gt=datetime.date.today())
        for booking in bookings:
            if date in booking.daterange():
                return True
        return False
    '''

    def __str__(self):
        return "Room #" + str(self.room_num)

class Guest(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    vip_num = models.IntegerField(default=-1)

    def __str__(self):
        return self.first + ' ' + self.last

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    start = models.DateField(default=datetime.date.today)
    length_of_stay = models.IntegerField(default=1)
    end = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0.0)

    def calc_stay(self):
        self.end = self.start + datetime.timedelta(days=self.length_of_stay)

    def book_room(self):
        self.room.occupied = True
        self.room.save()

    def daterange(self):
        return [self.start + datetime.timedelta(days=x) for x in range(1, self.length_of_stay + 1)]

    def calc_price(self):
        p = BASE_PRICE  # base price
        print(p)
        if self.room.oceanside():
            p += OCEANSIDE_SURCHARGE
        if self.room.suite():
            p += SUITE_SURCHARGE
        if self.guest.vip_num > 0:
            p *= 0.8
        p *= self.length_of_stay
        self.price = p
