# 파이썬 특강 Special Lecture

* 제목 : 모두를 위한 파이썬 Python for Everybody
* 목표
  - 파이썬을 처음 접하는 초보자를 대상으로,
  - 파이썬을 통해 해결할 수 있는 다양한 문제를 살펴보고, 
  - 자신의 전공 또는 관심 분야의 문제를 해결하기 위한 아이디어를 찾는다. 
* 특강 기록
  - 삼육대 파이썬 특강 : 2022년 05월 16일(월) 13:00~16:00
    - 강의노트 : [PDF](https://github.com/janggoons/python-sl/blob/main/20220516/python-sl-note_20220516.pdf) | [PPT](https://www.dropbox.com/s/e6unaqi6z30dkgm/python-sl-note_20220515.pptx?dl=0) 
  - 고교 연계 심화 프로젝트 - 파이썬 1일 특강 : 2022년 05월 29일(일) 13:00~15:00
    - 강의노트 : [PDF](https://github.com/janggoons/python-sl/blob/main/20220529/python-sl-note_20220529.pdf) | [PPT](https://www.dropbox.com/s/rbpc8fjsy0fj5so/python-sl-note_20220529.pptx?dl=0)

* 파이썬으로 할 수 있는 것과 하고 싶은 것을 모으고 나누기 [링크](https://docs.google.com/forms/d/e/1FAIpQLScxwKCe0JtHGvnfxwnblOhpKiTRoZiqUeIYqoAVrPYftBXprg/viewform)

* 실습 코드 안내
  - 20220516 
    - Sample01 : 워드클라우드 예제
    - Sample02 : 텍스트 추출 예제 
    - Sample03 : 이미지 크롤링 예제
    - Sample04 : 머신러닝(붓꽃 품종 분류) 예제
      * 구글 코랩 코드 [링크](https://colab.research.google.com/drive/1p5raTiNEnUj7oFIA1K-p7uU6bqXmug8P?usp=sharing)
  - 20220529
    - Sample01 : Hello World!
    - Sample02 : 이미지 크롤링 예제
 
* 실습 환경
  - 파이썬 3.10.4 : https://www.python.org/
  - 파이참 community 버전(무료) : https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows

* 트러블슈팅
  1. wordcloud 설치시 에러 메시지 중 다음 메시지가 뜬다면,
    - 컴퓨터에 C 컴파일러 설치하기(윈도우에서는 비주얼스튜디오 설치하기) https://visualstudio.microsoft.com/ko/downloads/
    - 별도 파일 다운로드 받아서 설치하기 https://noexpect.tistory.com/159
```python
...  'wordcloud.query_integral_image' extension error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/ ...
```
  
