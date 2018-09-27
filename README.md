# Kyonggi Web
2018.08.23~09.14 차세대융합기술연구원(Kyonggi web)

## Web Introduce
경기도민을 위한 공공플랫폼 중 하나인 실시간 정보 관제서비스<br>
openAPI를 이용하여 기상정보,미세먼지,인구수와 같은 공공데이터를 전달하는 웹 구축<br>

## Architecture
<li>Python 3.6.6<br>
<li>Django Framwork : 파이썬을 이용한 웹 구축 개발환경<br>
<li>Java Script & Ajax : 각 정보별 화면전환을 위한 인터페이스<br>
<li>QGIS : 경기도의 행정구역별 GeoJSON

## Open API
<li>Mapbox API : 지도를 HTML에 띄울 수 있는 API(Style변경을 위해 구글지도 사용안함)<br>
<li>openWeather API : 전세계 주요 도시별,위도경도별 실시간 날씨 조회<br>
<li>대기오염 정보조회 API: 공공데이터 포탈에서 제공, 시군구별 실시간 평균정보 조회<br>
<li>통계청 : 국가통계포탈에서 제공, 2018년 8월 주민등록인구현황의 엑셀자료를 json타입으로 변환하여 조회<br>


## Testing
<img src="https://user-images.githubusercontent.com/23578976/46118071-b6c6a500-c23f-11e8-8170-5ea3b0fb33a2.JPG" width="90%"></img>



