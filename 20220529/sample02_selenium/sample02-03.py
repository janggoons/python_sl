from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# 크롬 브라우저 실행하기
driver = webdriver.Chrome()

# 구글 이미지 검색 페이지로 이동하기
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# 이미지 검색 창에서 키워드 이미지 검색하기
elem = driver.find_element_by_name('q')
elem.send_keys("삼육고등학교")
elem.send_keys(Keys.RETURN)

# 검색한 이미지의 첫 번째 이미지를 불러오기
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
time.sleep(3)

# 첫 번째 이미지의 URL 주소를 이용하여 파일로 다운로드하기
img = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
imgUrl = img.get_attribute('src')
urllib.request.urlretrieve(imgUrl, "sample02-03.jpg")

# 브라우저 종료하기
# driver.close()

# 개선하기
# 1. 하나의 이미지가 아닌 여러개의 이미지를 다운로드 받고 싶다.