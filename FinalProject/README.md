# < 2022 Final Project >
## 사이버 강의를 들을 때 놓치는 영상, 레포트, 퀴즈를 알려주기위한 알림 봇 🤖

<li>프로젝트 명: Lms Notion Bot
<li>프로젝트 기간: 2022-05-23~

***
  
### Information
  
이 프로젝트는 텔레그램 봇(@LmsNotion_bot)에 ‘할 일’이라고 보내면 강의영상, 레포트, 퀴즈의 리스트를 자동으로 탐색한다. 셀레니움을 통해 정보를 가져오고, 봇을 이용해 하지 않은 것들은 제목과 함께 링크를 첨부하며 하라고 알려주고, 모두 했으면 완료했다고 메세지를 보내준다.
  
***
  
### Description
<li>lecfinder.py = 셀레니움을 이용해 LMS 크롤링하는 class 함수</li>
<pre><code> 
class LecFinder:
      def __init__(self):    
            강의 group_id 입력(주소창에 5자리 숫자로 존재)
            LMS 아이디 입력     
            LMS 비밀번호 입력
      
      def lec_report(self, driver):
  
      def lec_video(self, driver):
  
      def lec_quiz(self, driver):
  
      def report_result(self, driver):
  
      def video_result(self, driver):
  
      def quiz_result(self, driver):                                                                                                              
</code></pre>

<li>notiontelegrambot.py = 크롤링한 정보들을 텔레그램 봇을 통해 메세지 전달하는 class 함수</li>
<pre><code>
class NotionTelegramBot:
      def __init__(self):
            lecfinder.py 불러와 lf라고 지정
            Lms Notion Bot 토큰
            텔레그램 채팅 아이디 입력
            텔레그램 봇에 토큰 넘겨주기
            텔레그램으로부터 업데이트를 받아오기
      def handler(self, update, context):
  
      def send_telegram_msg(self, report):
      
      def main():
</pre></code>   

***
  
### Result
1. 먼저 봇을 검색해 '할일'이라고 치면 Selenium이 실행될 동안 '로딩중'이라는 메세지가 발송된다.
2. 탐색을 마치면, 결과를 사용자에게 보낸다. 
   해야할 일이 남았다면 그 카테고리의 이름과 기한, 링크를 첨부해 메세지를 보내고, 다 했다면 각 카테고리 별로 완료라는 메세지를 보낸다.

<img src="https://user-images.githubusercontent.com/93754504/172563833-955d5064-cbe7-4914-9622-c421792b9c74.png"  width="800" height="600"/>

#### 시현 동영상
<li>텔레그램 봇 시현: https://user-images.githubusercontent.com/93754504/172566878-57b5bc80-4eb8-4112-9966-e8a0e26985d1.mp4
<li>셀레니움 시현: https://user-images.githubusercontent.com/93754504/172567138-5b5005f5-4d11-4b4b-94df-f422c5d5bc4a.mp4

***

### Source
<li>텔레그램 봇 만들기 참고 : 
https://py-son.tistory.com/8
