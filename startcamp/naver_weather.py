# 날씨정보
import requests
city_name = "Seoul"
api_key = "b5d1091aff06331cfc04b142d0f73b0d"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

data = requests.get(url).json() # json 형태로 api  확인 가능
weather = data["weather"][0]["main"]
temp = data["main"]["temp"]-273.15
temp_min = data["main"]["temp_min"]-273.15
temp_max = data["main"]["temp_max"]-273.15
print(f"오늘의 온도는 {temp:1}도이고, 날씨는 {weather}이란다!\n최저온도는 {temp_min}, 최고온도는 {temp_max}래!")