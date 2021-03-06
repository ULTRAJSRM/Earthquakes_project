from django.db import models


class Earthquake(models.Model):
    des_name = models.CharField(max_length=100)
    num_magnitude = models.DecimalField(max_digits=3, decimal_places=2)
    des_place = models.CharField(max_length=200)
    flag_alarm = models.BooleanField()
    des_country = models.CharField(max_length=50, blank=True, null=True)
    time_detected = models.DateTimeField()
    time_created_db = models.DateTimeField(auto_now_add=True)
    time_updated_db = models.DateTimeField(auto_now=True)

    def  __str__(self):
        '''To see the earthquake name in djangoAdmin when table is called'''
        return self.des_name