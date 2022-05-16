import numpy as np                  # pip install numpy
from PIL import Image
from wordcloud import WordCloud     # pip install wordcloud
import matplotlib.pyplot as plt     # pip install matplotlib

# .txt 파일에 있는 텍스트를 가져오기
lyrics = open('source.txt', 'r', encoding='utf-8-sig')
lyrics = lyrics.read()
# print(lyrics) # 읽어온 텍스트 출력하기

# 워드클라우드의 모양과 폰트 설정
mask = np.array(Image.open('./mask.png'))

# 워드클라우드 생성
wc = WordCloud(background_color='white', mask=mask, width=800, height=800)
wc.generate(lyrics)

# 워드클라우드 저장
f = plt.figure(figsize=(8,8))
plt.axis('off')
plt.imshow(wc)
f.savefig('./sample01-01_result.png')

# 더 해보기
# 1. 다른 텍스트를 수집해서 워드클라우드로 만들어보기
# 2. 워드클라우드의 폰트, 색, 마스크 등을 바꿔보기
# 3. 불필요한 단어 제거하고 워드클라우드 만들기
