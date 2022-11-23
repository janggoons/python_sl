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
elem.send_keys("남궁민")
elem.send_keys(Keys.RETURN)

# 작은 섬네일 이미지 찾기
images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
print(f"로드된 이미지 개수: {len(images)}")
# 파일 다운로드 받기 위한 준비

img_file_list = ['jpg', 'JPG', 'jpeg', 'png', 'PNG', 'gif', 'GIF']

# 이미지 파일을 다운로드 받아서 새로운 이름으로 저장하기를 반복하기
for i, image in enumerate(images):  
  image.click()
  time.sleep(3)
  imgUrl = driver.find_element(By.CSS_SELECTOR, "img.n3VNCb.KAlRDb").get_attribute("src")
  print(f"{i}번 이미지 URL주소:{imgUrl}")
  ext = imgUrl.split('.')[-1]
  if ext in img_file_list:
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgUrl, str(i) + ".jpg")

# 웹 브라우저 닫기
driver.close()
