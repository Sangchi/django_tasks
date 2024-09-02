from django.db import models

#prashanat@gmail.com
# Create your models here.


class Car(models.Model):

    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:

        return self.car_name
    

class User(models.Model):

    user_name=models.CharField(max_length=500)
    booking_car= models.ForeignKey(Car, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user_name

