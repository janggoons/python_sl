# pip install beautifulsoup4
# pip install pandas
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://www.syu.ac.kr/academic/academic-notice/")
soup = BeautifulSoup(html, 'html.parser')

tag_tbody = soup.find('tbody')
# print(tag_tbody)
# print(tag_tbody.find_all('tr'))
# post = tag_tbody.find('tr')
# print(post.find('span', attrs={'class':'tit'}).string)
result = []
for post in tag_tbody.find_all('tr'):
    post_title = post.find('span', {'class':'tit'})
    # print(post_title.text)
    post_writer = post.find('td', {'class':'step3'})
    # print(post_writer.text)
    post_date = post.find('td', {'class':'step4'})
    # print(post_date)
    result.append([post_title.text] + [post_writer.text] + [post_date.text])

# print(result)

# 크롤링한 데이터 저장하기
post_tbl = pd.DataFrame(result, columns=('title', 'writer', 'date'))
# print(post_tbl)

post_tbl.to_csv('./post.csv', encoding='cp949', mode='w', index=True)


# 개선하기
# 1. 게시판의 모든 페이지에 해당하는 데이터 가져오기