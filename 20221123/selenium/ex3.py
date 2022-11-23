from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# 웹 브라우저 열기
driver = webdriver.Chrome()

# 웹 브라우저에서 구글 이미지 웹 페이지로 이동하기
driver.get("https://www.google.co.kr/imghp?hl=en&tab=ri&ogbl")

# 검색창에 키워드 입력하고 엔터치기
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("octonauts coloring")
elem.send_keys(Keys.RETURN)

# 첫 번째 섬네일 이미지 클릭하기
driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[0].click()
time.sleep(3)

# 오른쪽에 큰 섬네일 이미지의 파일 정보 가져오기
img = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb")
imgUrl = img.get_attribute('src')

# 파일을 다운로드 받아서 새로운 이름으로 저장하기
# https://www.inflearn.com/questions/439440
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozila/5.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(imgUrl, '0001.jpg')

# 웹 브라우저 닫기
driver.close()