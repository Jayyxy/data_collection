import requests # 웹 페이지 요청을 위해 
from bs4 import BeautifulSoup # class 불러오기 , 가져온 문서에서 데이터 추출을 위해
import time

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


data = []


for page in range(1,20) :
    url =  f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}'
    response = requests.get(url) # 해당 URL에 대해 요청을 하고, 응답을 받는다
    bs = BeautifulSoup(response.text)
    entire = bs.select("div.col-lg-9 > div.row div.col-md-4.col-xl-4.col-lg-4")
# print(entire) # 잘 파싱했는지 확인(1)

    for product in entire : 
        detailed = product.select_one("div.product-wrapper")
        img_url = detailed.select_one("img.img-fluid")["src"]

        caption = detailed.select_one("div.caption")
        price = caption.select_one("h4.price span").get_text(strip=True)
        product_name = caption.select_one("h4 a.title").get_text(strip=True)
        detail_product_url = caption.select_one("h4 a.title")['href']
        spec = caption.select_one("p.description").get_text(strip=True)
        
        rating = detailed.select_one("div.ratings")
        star_count = rating.select_one("p:nth-child(2)")["data-rating"]
        review = rating.select_one("p.review-count span").get_text(strip=True)

        data.append({
            "name" : product_name,
            "price" : price ,
            "spec" : spec ,
            "img_url" : img_url ,
            "detail_url" : detail_product_url,
            "star_count" : star_count ,
            "review" :review 
        })
    time.sleep(1)

for i in data :
    print(data)
    print("==============")

print(len(data))