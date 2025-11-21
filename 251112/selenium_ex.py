'''
Beautfulsoup 의 한계
- 완성된 웹페이지 전용
- 동적인 페이지 처리가 어려움 

-> Selenium

'''



'''
Selenium 사용
- 터미널 ctrl + ~ 
- pip install selenium

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

options = Options()
options.add_experimental_option("detach",True)


# 객체 생성
driver = webdriver.Chrome(options=options)

# 특정 주소에 대한 
url = "https://www.naver.com/"
driver.get(url) # 해당 URL 
time.sleep(1) # 동작 사이마다 대기시간 설정 (2초)

# 검색어 입력
query= driver.find_element(By.ID, "query")
query.send_keys("데이터 엔지니어링") # 입력한 키워드와 동일한 문자 추출
time.sleep(1)

# =================
# 1) 엔터로 검색
# =================
query.send_keys(Keys.ENTER)

# =================
# 2) 버튼 클릭으로 검색
# =================
#search_btn= driver.find_element(By.CSS_SELECTOR, "#search-btn") # 선택자 문법으로 검색한다고 설정
#search_btn.click()

# Xpath방식 
# : 태그가 없어도 키워드로 검색 가능 

# ---------------------------------------------------------------------------------------------
# 로그링 창으로 이동하여 id pass 입력하기

login_btn = driver.find_element(By.CSS_SELECTOR,"a.MyView-module__link_login___HpHMW")
login_btn.click()
time.sleep(1)

id = driver.find_element(By.ID, "id")
id.send_keys()
time.sleep(1)
pw = driver.find_element(By.ID, "pw")
pw.send_keys()
time.sleep(1)

login_page_btn = driver.find_element(By.CSS_SELECTOR)
login_page_btn.click()
