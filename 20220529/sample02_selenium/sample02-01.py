from selenium import webdriver

# 크롬 브라우저 실행하고, google.com 사이트로 이동하기
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://google.com")
