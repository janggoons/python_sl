# 파이썬 특강 Special Lecture

* 제목 : 모두를 위한 파이썬 Python for Everybody
* 목표
  - 파이썬을 통해 해결할 수 있는 다양한 문제를 살펴보고, 
  - 자신의 전공 또는 관심 분야의 문제를 해결하기 위한 아이디어를 찾는다. 
* 일시 : 2022년 05월 16일(월) 13:00~16:00

* 실습 코드 안내
  - Sample01 : 워드클라우드 예제
  - Sample02 : 텍스트 추출 예제 
  - Sample03 : 이미지 크롤링 예제
  - Sample04 : 머신러닝(붓꽃 품종 분류) 예제
    * 구글 코랩 코드 [링크](https://colab.research.google.com/drive/1p5raTiNEnUj7oFIA1K-p7uU6bqXmug8P?usp=sharing)
  - 오른쪽 상단의 Code(녹색버튼) > Download ZIP 으로 다운로드 후 압축해제

* 실습 환경
  - 파이썬 3.10.4 : https://www.python.org/
  - 파이참 community 버전(무료) : https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows

* 강의 자료 : [PDF](https://github.com/janggoons/python-sl/blob/main/python-sl-note_20220515.pdf) | [PPT](https://www.dropbox.com/s/e6unaqi6z30dkgm/python-sl-note_20220515.pptx?dl=0)

* 트러블슈팅
  - wordcloud 설치시 에러 메시지 중 다음 메시지가 뜬다면,
```python
...  'wordcloud.query_integral_image' extension error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/ ...
```
  - 1) 컴퓨터에 C 컴파일러 설치하기(윈도우에서는 비주얼스튜디오 설치하기) https://visualstudio.microsoft.com/ko/downloads/
  - 2) 별도 파일 다운로드 받아서 설치하기 https://noexpect.tistory.com/159
