from django.db import models
import datetime
from django.utils import timezone

class TimePunch(models.Model):
    name= models.CharField(max_length=200)
    school= models.CharField(max_length=200)
    hours= models.IntegerField()
    dateOfwork= models.DateField()
    dateOfentry= models.DateField()

    def __str__(self):
        return self.name, self.school,self.hours,self.dateOfwork,self.dateOfentry>= timezone.now() -datetime.timedelta(days=1)
