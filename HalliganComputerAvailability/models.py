from django.db import models
from datetime import datetime
from django.contrib import admin

# Create your models here.

class Computer(models.Model):
    OFF = 'OFF'
    INUSE = 'INUSE'
    AVAILABLE = 'AVAILABLE'
    ERROR = 'ERROR'

    CHOICES = [OFF, INUSE, AVAILABLE]

    STATUS_CHOICES = (
        (OFF, 'Powered Off'),
        (INUSE, 'In Use'),
        (AVAILABLE, 'Currently Available'),
        (ERROR, 'Error')
    )
    ComputerNumber = models.CharField(max_length=7,
                                      primary_key=True)#Primary Key
    RoomNumber = models.IntegerField()
    Status = models.CharField(max_length=9,
                              choices=STATUS_CHOICES,
                              default=AVAILABLE)

admin.site.register(Computer)


class Lab(models.Model):
    ClassName = models.CharField(max_length=30)
    RoomNumber = models.IntegerField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    StartDate = models.DateField()
    EndDate = models.DateField()
    DayOfWeek = models.IntegerField(max_length=1)

    def is_lab_in_session(self):
        CurrTime = datetime.now().time()
        CurrDate = datetime.now().date()

        if(self.StartDate < CurrDate < self.EndDate
           and self.StartTime < CurrTime < self.EndTime):
            return True

        return False

admin.site.register(Lab)






