from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹 브라우저 열기
driver = webdriver.Chrome()

# 웹 브라우저에서 구글 이미지 웹 페이지로 이동하기
driver.get("https://www.google.co.kr/imghp?hl=en&tab=ri&ogbl")

# 검색창에 키워드 입력하고 엔터치기
# https://selenium-python.readthedocs.io/locating-elements.html
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("octonauts coloring")
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
elem.send_keys(Keys.RETURN)

# 웹 브라우저 닫기
driver.close()