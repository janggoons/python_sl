from wordcloud import WordCloud     # pip install wordcloud
import matplotlib.pyplot as plt     # pip install matplotlib
# import matplotlib.font_manager as fm # 폰트 확인시에만 필요

# .txt 파일에 있는 텍스트를 가져오기
lyrics = open('./source.txt', 'r', encoding='utf-8-sig')
lyrics = lyrics.read()

# 컴퓨터에 설치된 고딕 폰트 확인
# for f in fm.fontManager.ttflist:
#     if 'Gothic' in f.name:
#         print(f.fname)

# 워드클라우드의 모양과 폰트 설정
font_path = 'C:\\WINDOWS\\Fonts\\NanumGothicLight.ttf'

# 제외할 단어 추가하기
stopwords = {'나'}

# 워드클라우드 생성
wc = WordCloud(font_path=font_path, background_color='white', width=800, height=800, stopwords=stopwords)
wc.generate(lyrics)

# 워드클라우드 저장
f = plt.figure(figsize=(8,8))
plt.axis('off')
plt.imshow(wc)
f.savefig('./sample01-02_result.png')