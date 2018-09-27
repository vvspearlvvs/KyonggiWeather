from django.shortcuts import render
from django.shortcuts import render_to_response
from urllib.request import urlopen
import json

import xlrd
from collections import OrderedDict


from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET

"""
weatherurl = 'http://api.openweathermap.org/data/2.5/box/city?bbox=126.7,36.9,127.8,38.5,11&cluster=yes&format=json&APPID=45177ff490cc791de1def08e071936b1'
wdata = urlopen(weatherurl).read()
jwdata = json.loads(wdata)
kwdata = jwdata['list']
js_data = json.dumps(kwdata)

airurl='https://api.waqi.info/map/bounds/?latlng=39.379436,116.091230,40.235643,116.784382&token=2089b05319f581b79a51540823d2984060a0127e'
adata=urlopen(airurl).read()
jadata=json.loads(adata)
kadata=jadata['data']
#print(kadata)
"""


class Data:
    cityid = ['1843082', '1842485', '1841909', '1948005', '1841810', '1841988', '1842030', '1842936', '1897122',
              '1838716', '1897000', '1835553', '1846918', '1846912', '1842030', '1832847', '1832830', '1832743',
              '1832697', '1839652', '1832427', '1842030', '1833788', '1843702', '1840898', '1838431', '1897007',
              '1843847', '1843847', '1843847', '1843847']

    def getWeather(self):
        # weatherurl = 'http://api.openweathermap.org/data/2.5/box/city?bbox=126.7,36.9,127.8,38.5,11&cluster=yes&format=json&APPID=45177ff490cc791de1def08e071936b1'

        print(len(self.cityid))
        kyonggiweatehr = []
        for i in range(len(self.cityid)):
            weatherurl = 'http://api.openweathermap.org/data/2.5/weather?id=' + self.cityid[i] + '&APPID=45177ff490cc791de1def08e071936b1'
            wdata = urlopen(weatherurl).read()
            jwdata = json.loads(wdata)
            kwdata = json.dumps(jwdata, ensure_ascii=False)  # kwdata : json string
            json_array = json.loads(kwdata)
            kyonggiweatehr.append(json_array)
        print(json.dumps(kyonggiweatehr, ensure_ascii=False))
        print(len(kyonggiweatehr))

        return json.dumps(kyonggiweatehr, ensure_ascii=False)

    def getAir(self):
        airurl = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=afYQPSYR8BIhn6sZe4InwLX8vBfZfXYbKkVBHU9CAIXmTbqvc4fcn6sinGJTQ9529dAwEW2XgTDC5fz7pKEzAg%3D%3D&numOfRows=100&pageSize=100&pageNo=1&startPage=1&sidoName=%EA%B2%BD%EA%B8%B0&searchCondition=HOUR&_returnType=json'
        adata = urlopen(airurl).read()
        jadata = json.loads(adata)
        kadata = jadata['list']
        kadata = json.dumps(kadata, ensure_ascii=False)
        print(kadata)

        return kadata

    def getPop(self):
        pop_list = []

        wb = xlrd.open_workbook('D:/PycharmProject/DjangoProject/Weather/Weathersite/Weatherapp/templates/Weatherapp/kyonggiPopulation.xlsx')
        sh = wb.sheet_by_index(0)
        for rownum in range(3, sh.nrows):
            row_value = sh.row_values(rownum)
            data = {"seq": rownum - 2,
                    "cityName": row_value[0],
                    "popNum": row_value[1],
                    "Man": row_value[3],
                    "Woman": row_value[4],
                    }
            pop_list.append(data)
        print(pop_list)

        #print(json.dumps(pop_list, ensure_ascii=False))

        return json.dumps(pop_list, ensure_ascii=False)

@require_GET
def weather_url(request):
    data = Data();
    #return HttpResponse(json.dumps(kyonggiweatehr, ensure_ascii=False), content_type="application/json; charset=utf-8")
    return HttpResponse(data.getWeather(), content_type="application/json; charset=utf-8")
    # return HttpResponse(json.dumps(data.getWeather(), ensure_ascii=False), content_type="application/json; charset=utf-8")


@require_GET
def air_url(request):
    data = Data();
    return HttpResponse(data.getAir(), content_type="application/json; charset=utf-8")
    # return HttpResponse(json.dumps(data.getAir(), ensure_ascii=False), content_type="application/json; charset=utf-8")

@require_GET
def pop_url(request):
    xldata = Data();
    return HttpResponse(xldata.getPop(), content_type="application/json; charset=utf-8")



def main_html(request):
    #return render(request, 'Weatherapp/Mainmap.html')
    return render(request, 'Weatherapp/Mainmap2.html')

# Create your views here.
def btm_html(request):
    data = Data();
    content = {'weather_list': data.getWeather(), 'air_list': data.getAir(), 'population_list': data.getPop()}
    #return render(request, 'Weatherapp/Mainmap.html', content)
    return render(request, 'Weatherapp/Mainmap2.html', content)
