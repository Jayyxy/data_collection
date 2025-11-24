import requests # 웹 페이지 요청을 위해 
from bs4 import BeautifulSoup # class 불러오기 , 가져온 문서에서 데이터 추출을 위해


url =  'https://webscraper.io/test-sites/e-commerce/static'
response = requests.get(url) # 해당 URL에 대해 요청을 하고, 응답을 받는다
bs = BeautifulSoup(response.text)

# =====================================
# 원하는 상품 가져와서 출력하기 
# 1_ 카트 아이콘 사진의 주소
# 2_ 상품 이름
# 3_ 가격
# 4_ 상세 스펙 텍스트
# 5_ 리뷰 개수
# 6_ 별의 개수
# 7_ 각 상품의 상품의 상세 페이지 주소 URL 
# =====================================

# 1_ 카트 아이콘 사진의 주소
''' 원하는 이미지를 별도로 가져오게 하기'''
img_card = bs.select('img')
print(img_card)


img_url = bs.select_one('img[alt="item"]')
print(img_url.get('src'))

for i in img_card:
    cart_img = i.get('src')

print(cart_img)


# 2_ 상품 이름

productes = bs.select('h4 a.title')
print(productes)

print(productes[2].get_text())


# 3_ 가격
prices = bs.select('div.caption h4 span')
print(prices)

print(prices[2].get_text(strip=True))

