# 코스피
import requests
from bs4 import BeautifulSoup 

url = "https://finance.naver.com/sise/"
response = requests.get(url).text
# print(response)

data = BeautifulSoup(response, 'html.parser')
select = data.select_one("#KOSPI_now").text
print(select)
