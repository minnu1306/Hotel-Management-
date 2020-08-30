from django.db import models

# Create your models here.
class RNac(models.Model):
    roomno= models.IntegerField()
    occopied=models.BooleanField(default=False)

    def __str__(self):
        return str(self.roomno)

class Rac(models.Model):
    roomno= models.IntegerField()
    occopied=models.BooleanField(default=False)

    def __str__(self):
        return str(self.roomno)

class Dac(models.Model):
    roomno= models.IntegerField()
    occopied=models.BooleanField(default=False)

    def __str__(self):
        return str(self.roomno)
