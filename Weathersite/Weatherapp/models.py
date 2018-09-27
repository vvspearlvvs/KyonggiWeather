from django.db import models
from pyowm import OWM
API_KEY = '45177ff490cc791de1def08e071936b1'
owm = OWM(API_KEY)

# Create your models here.
obs=owm.weather_at_coords(37.2941607,127.0454037) #위도경도로 날씨찾기
l=obs.get_location()
w=obs.get_weather()

class Weather(models.Model):
    #location_lat = models.FloatField()
    #location_lon = models.FloatField()
    status=models.CharField(max_length=30)
    temp=models.FloatField()
    #maxtemp=models.FloatField()
    #mintetmp=models.FloatField()
    #clouds = models.IntegerField()
    #humidity = models.IntegerField()

    def __str__(self):
        return self.name

    def set_weather_status(self):
        self.status=w.get_status()

    def set_weather_temp(self):
        self.temp = w.get_temperature(unit='celsius')['temp']

    def get_weather_status(self):
        return self.status

    def get_weather_temp(self):
        return self.temp