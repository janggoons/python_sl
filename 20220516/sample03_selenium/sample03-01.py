from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 브라우저 실행하고, python.org 사이트로 이동하기
driver = webdriver.Chrome()
driver.get("http://www.python.org")

# 검색창에 pycon 을 입력하여 검색하기
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# 브라우저 종료하기
# driver.close()

# 개선하기
# 1. 다른 검색 사이트에서 다른 키워드로 검색하고 싶다.


