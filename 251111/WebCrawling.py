# 터미널에 (ctrl + ~)
# pip install request pip install bs4 설치 


# 라이브러리 불리오기 
import requests # 웹 페이지 요청을 위해 
from bs4 import BeautifulSoup # class 불러오기 , 가져온 문서에서 데이터 추출을 위해


'''
원하는 요소의 html 코드를 찾는 법 
1. 개발자 코드 F12 -> 왼쪽 상단 화살표 : 원하는 요소에 갖다대면 해당 요소 활성화 
2. 요소 우클릭 -> 검사  : 해당 요소의 html 코드 활성화
'''

url = "https://www.scrapethissite.com/pages/simple/" # 크롤링 하고자 하는 URL 
response = requests.get(url) # get()요청 : 해당 URL에 대해 요청을 하고, 응답을 받는다
bs = BeautifulSoup(response.text)
# 응답으로 받은 결과 중에서 HTML 문서 텍스트를 가져와서 이것을 bs 객체로 생성
# 크롤링 작업을 bs 객체를 통해 수행한다는 뜻 

# =============================================
# 1. Andorra 가져오기 
# =============================================
##  print(bs.select("h3.country-name")) #여러가지 가져옴 

## 한가지만 사용하고 싶을 때 : select_one 사용 (태그 포함) 

# select 함수의 결과는 list이다. 
andorra = bs.select_one("h3.country-name")
print(andorra.get_text(strip=True)) # strip = True : 공백, 줄바꿈 문자처리

# =============================================
# 2. 전 세계 나라의 정보(이름, 수도, 인구수, 면적) 추출하기  
# =============================================
# row 바깥에도 검색할수 있어서   ~ 도 추가 

# col-md4가 있어야 하위 country를 검색할수 있음 
countries = bs.select("div.row div.col-md-4")
print(countries)

# 크롤링한 여러개의 값들을 딕셔너리 형태로 만들기 
for country in countries :
    name = country.select_one("h3.country-name").get_text(strip=True)
    country_info = country.select_one("div.country-info")
    capital = country_info.select_one("span.country-population").get_text(strip=True)
    population = country_info.select_one("span.country-population").get_text(strip=True)
    area = country_info.select_one("span.country-area").get_text(strip=True)
    print(f"나라 이름: {name}, 수도:{capital}, 인구: {population}, 면적: {area}")



