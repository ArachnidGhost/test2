from django.db import models
import datetime


class UserData(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=220)
    number = models.IntegerField()
    email = models.EmailField()
    Topic = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.time:
            self.time = self.round_time(self.time)
        super().save(*args, **kwargs)

    @staticmethod
    def round_time(dt):
        dt = dt + datetime.timedelta(seconds=dt.second, microseconds=dt.microsecond)
        return dt - datetime.timedelta(minutes=dt.minute % 15, seconds=dt.second, microseconds=dt.microsecond)