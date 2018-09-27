
from urllib.request import urlopen
import xml.etree.ElementTree as eltree
import json

import xlrd
from collections import OrderedDict

wb = xlrd.open_workbook('C:/Users/wearable/Desktop/KyonggiLayer/kyonggiPopulation.xlsx')
sh = wb.sheet_by_index(0)
#print(sh.nrows)

pop_list=[]

for rownum in range(3, sh.nrows):
    population = OrderedDict()
    row_value = sh.row_values(rownum)
    data = {"seq": rownum-2,
            "cityName": row_value[0],
            "popNum": row_value[1],
            "Man": row_value[3],
            "Woman": row_value[4]}
    print(data)
    pop_list.append(data)

print(json.dumps(pop_list, ensure_ascii=False))

"""
    population['cityName'] = row_value[0]
    population['popNum'] = row_value[1]
    population['Man'] = row_value[3]
    population['Woman'] = row_value[4]

    pop_list.append(population)
  

weatherurl = 'http://api.openweathermap.org/data/2.5/box/city?bbox=126.7,36.9,127.8,38.5,11&cluster=yes&format=json&APPID=45177ff490cc791de1def08e071936b1'
wdata = urlopen(weatherurl).read()
jwdata = json.loads(wdata)
kwdata = jwdata['list']
js_data = json.dumps(kwdata)
"""

"""
air_arr = []
city_list = ['Hwaseong','Suwon','Pyeongtaek','Goyang']

for i in city_list:
    airurl='http://api.airvisual.com/v2/city?country=South%20Korea&state=Gyeonggi-do&city='+i+'&key=pzTbH7FXzbYAw3AjB'
    adata = urlopen(airurl).read()
    jadata = json.loads(adata)
    kadata = jadata['data']
    print(kadata)
"""

"""
airurl='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?serviceKey=afYQPSYR8BIhn6sZe4InwLX8vBfZfXYbKkVBHU9CAIXmTbqvc4fcn6sinGJTQ9529dAwEW2XgTDC5fz7pKEzAg%3D%3D&numOfRows=100&pageSize=100&pageNo=1&startPage=1&sidoName=%EA%B2%BD%EA%B8%B0&searchCondition=HOUR&_returnType=json'
adata = urlopen(airurl).read()
jadata = json.loads(adata)
kadata = jadata['list']
print(kadata)
"""
