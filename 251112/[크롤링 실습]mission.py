
'''
[크롤링 미션]
모든 페이지에 있는 데이터를 크롤링하여 딕셔너리를 원소로 갖는 리스트 형태로 결과를 출력하세요.
{
  Team Name : ...,
  Year : ...,
  Wins : ...,
  Losses : ...,
  OT Losses : ...,
  Win % : ...,
  Goals For(GF) : ...,
  Goals Against(GA) : ...,
  + / - : ...
} 


특히 'Win %'와 '+ / -' 의 데이터의 경우 초록색 글씨는 괄호에 success를 붙여서, 빨간색 글씨는 danger를 붙인 결과로 만드세요.
ex) 
win : 0.55(success)
win : 0.312(danger)

+ / - : 35(success)
+ / - : -38(danger)
 
https://www.scrapethissite.com/pages/forms/

'''


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

url = "https://www.scrapethissite.com/pages/forms/" 


for row in rows :
    print 