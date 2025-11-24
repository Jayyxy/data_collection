import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
res = requests.get(url)

bs = BeautifulSoup(res.text)
# print(bs)
entire = bs.select("div.col-lg-9 > div.row div.col-md-4.col-xl-4.col-lg-4")
print(len(entire))

data = []
for product in entire: # product 변수 = 상품 하나에 대한 영역 요소
    detailed = product.select_one("div.product-wrapper")

    img_url = detailed.select_one("img.img-fluid")["src"]
    # /images/test-sites/e-commerce/items/cart2.png

    # caption element
    caption = detailed.select_one("div.caption") # caption 영역 추출


    price = caption.select_one("h4.price span").get_text(strip=True)
    # $416.99
    product_name = caption.select_one("h4 a.title").get_text(strip=True)
    # Packard 255 G2

    detail_product_url = caption.select_one("h4 a.title")['href']
    # /test-sites/e-commerce/static/product/31
    '''
    caption.select_one("h4 a.title")
    -> 
    <a href="/test-sites/e-commerce/static/product/31" class="title" title="Packard 255 G2" itemprop="name">
						Packard 255 G2
					</a>
    '''
    spec = caption.select_one("p.description").get_text(strip=True)
    # 15.6", AMD E2-3800 1.3GHz, 4GB, 500GB, Windows 8.1

    # rating element
    rating = detailed.select_one("div.ratings") # ratings 영역 가져오기

    review = rating.select_one("p.review-count span").get_text(strip=True)
    # 2 
    star_count = rating.select_one("p:nth-child(2)")["data-rating"]
    # 2
    '''
    rating.select_one("p:nth-child(2)")
    ->
    <p data-rating="2">
										<span class="ws-icon ws-icon-star"></span>
										<span class="ws-icon ws-icon-star"></span>
									</p>
    '''
    data.append({
        "name" : product_name,
        "price" : price,
        "spec" : spec,
        "img_url" : img_url,
        "detail_url" : detail_product_url,
        "star_count" : star_count,
        "reviews" : review
    })
    # print(img_url, price, product_name, detail_product_url, spec, star_count, review)

for i in data:
    print(i)
    print()