# < 2022 Final Project >
## LMS로 강의를 들을 때 놓치는 영상, 레포트, 퀴즈를 알려주기위한 알림 봇 🤖

<li>프로젝트 명: Lms Notion
<li>프로젝트 기간: 2022-05-23~

***
  
### Information
  
이 프로젝트는 텔레그램 봇(@LmsNotion_bot)에 ‘할 일’이라고 보내면 강의영상, 레포트, 퀴즈의 리스트를 자동으로 탐색한다. 셀레니움을 통해 정보를 가져오고, 봇을 이용해 하지 않은 것들은 제목과 함께 링크를 첨부하며 하라고 알려주고, 모두 했으면 완료했다고 메세지를 보내준다.
  
***
  
### Description
#### <li>lecfinder.py = 셀레니움을 이용해 LMS 크롤링하는 class 함수</li>
<pre><code> 
class LecFinder:
      def __init__(self):    
            - 강의 group_id 입력(주소창에 5자리 숫자로 존재)
            - LMS 아이디 입력     
            - LMS 비밀번호 입력
            
      def lec_report(self, driver):
            - 입력된 group_id로 format시켜 LMS 레포트 사이트 주소를 가져온다.
            - elements = 위의 사이트에서 레포트를 내용을 가지고있는 부분을 css selector로 가져온다.
            - elements의 개수를 세고 1개 이상이면 if문을 시행한다.
            - 과제제목, 제출기한, 제출여부를 포함시킬 빈 리스트를 생성한다.
            - for문을 이용해 사이트에서 제목, 기한, 제출여부의 정보를 가져와 각각의 리스트에 추가해준다.
            - for문이 끝나고 pandas의 DataFrame을 이용하여 각 리스트들을 테이블화한다.
            - 이 테이블들은 df로 정의되며 위의 if문을 만족시킬 때 df를 돌려준다.
            - 레포트 개수가 없다면 '레포트는 없습니다.'라는 문자열을 돌려준다.
            
      def lec_video(self, driver):
            - 입력된 group_id로 format시켜 LMS 출석부의 영상부분 사이트 주소를 가져온다.
            - elements = 위의 사이트에서 영상의 내용을 가지고있는 부분을 css selector로 가져온다.
            - elements의 개수를 세고 1개 이상이면 if문을 시행한다.
            - 강의제목, 인정기간, 출석여부를 포함시킬 빈 리스트를 생성한다.
            - for문을 이용해 사이트에서 제목, 기간, 출석여부의 정보를 가져와 각각의 리스트에 추가해준다.
            - for문이 끝나고 pandas의 DataFrame을 이용하여 각 리스트들을 테이블화한다.
            - 이 테이블들은 ds로 정의되며 위의 if문을 만족시킬 때 ds를 돌려준다.
            - 레포트 개수가 없다면 '강의는 없습니다.'라는 문자열을 돌려준다.
            
      def lec_quiz(self, driver):
             - 입력된 group_id로 format시켜 LMS 퀴즈 사이트 주소를 가져온다.
            - elements = 위의 사이트에서 영상의 내용을 가지고있는 부분을 css selector로 가져온다.
            - elements의 개수를 세고 1개 이상이면 if문을 시행한다.
            - 퀴즈제목, 기간, 제출여부를 포함시킬 빈 리스트를 생성한다.
            - for문을 이용해 사이트에서 제목, 기간, 제출여부의 정보를 가져와 각각의 리스트에 추가해준다.
            - for문이 끝나고 pandas의 DataFrame을 이용하여 각 리스트들을 테이블화한다.
            - 이 테이블들은 dc로 정의되며 위의 if문을 만족시킬 때 dc를 돌려준다.
            - 레포트 개수가 없다면 '퀴즈는 없습니다.'라는 문자열을 돌려준다.
            
      def report_result(self, driver):
            - lec_report의 return값을 df라고 저장한다.
            - 그 결과가 문자열이라면 '레포트는 없습니다.'라는 문자열을 돌려준다.
            - 아니라면 먼저 과제제목 테이블의 요소 개수를 세고 확인을 위한 count_correct라는 빈 리스트를 생성한다.
            - 만약 df[제출여부]가 '미제출'이라면 각 df[과제제목]과 df[제출기간]을 리스트에 포함한다.
            - 그 후 count_correct리스트의 원소 개수가 1개 이상이라면 리스트를 돌려주고, 아니라면 '레포트는 없습니다'라는 문자열을 돌려준다.
            
      def video_result(self, driver):
            - lec_videot의 return값을 ds라고 저장한다.
            - 그 결과가 문자열이라면 '영상은 없습니다.'라는 문자열을 돌려준다.
            - 아니라면 먼저 강의제목 테이블의 요소 개수를 세고 확인을 위한 count_correct라는 빈 리스트를 생성한다.
            - 만약 ds[출석여부]가 '결석'이라면 각 ds[강의제목]과 ds[인정기간]을 리스트에 포함한다.
            - 그 후 count_correct리스트의 원소 개수가 1개 이상이라면 리스트를 돌려주고, 아니라면 '영상은 없습니다'라는 문자열을 돌려준다.
            
      def quiz_result(self, driver):      
            - lec_quiz의 return값을 dc라고 저장한다.
            - 그 결과가 문자열이라면 '퀴즈는 없습니다.'라는 문자열을 돌려준다.
            - 아니라면 먼저 퀴즈제목 테이블의 요소 개수를 세고 확인을 위한 count_correct라는 빈 리스트를 생성한다.
            - 만약 df[제출여부]가 '미제출'이라면 dc[퀴즈제목]과 dc[기간]을 리스트에 포함한다.
            - 그 후 count_correct리스트의 원소 개수가 1개 이상이라면 리스트를 돌려주고, 아니라면 '퀴즈는 없습니다'라는 문자열을 돌려준다.           
</code></pre>

#### <li>notiontelegrambot.py = 크롤링한 정보들을 텔레그램 봇을 통해 메세지 전달하는 class 함수</li>
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

<img src="https://user-images.githubusercontent.com/93754504/172797318-4e0d7af0-8833-4814-90a9-2509c5ab0ea7.png"  width="570" height="600"/>

#### 시연 동영상
<li>텔레그램 봇 시연: https://user-images.githubusercontent.com/93754504/172798687-c3c27d34-8102-448d-a7bc-cab8e86bbf4d.mp4
<li>셀레니움 시현: https://user-images.githubusercontent.com/93754504/172567138-5b5005f5-4d11-4b4b-94df-f422c5d5bc4a.mp4

***

### Source
<li>텔레그램 봇 만들기 참고 : 
https://py-son.tistory.com/8
