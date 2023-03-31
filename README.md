# 응용소프트웨어개발

## Description
- 과목: 프로그래밍원리와실습
- 학기: 2022년도 1학기 학과 전공 수업
- 지도: 김태곤 교수님

## HomeWork

<details>
<summary>과제03 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C03'>(Go)</a></summary>

  - 원의 면적구하기(반지름 입력받아 면적 출력) | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C03/03-1.py">03-1.py</a><br>
  - 칼로리 구하기(과일마다 섭취 g를 받아 칼로리 출력) | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C03/03-2.py">03-2.py</a><br>
  - 두 지점 사이 거리 구하기(x1, y1, x2, y2 입력받아 거리 출력) | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C03/03-3.py">03-3.py</a><br>
</details>

<details>
<summary>과제04 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C04'>(Go)</a></summary>

  - x, y를 입력받아 사사분면 출력하기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C04/04-1.py">04-1.py</a><br>
  - <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C03/03-2.py">과제#3-2</a>에서 칼로리 계산 프로그램을 딕셔너리로 이용 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C04/04-2.py">04-2.py</a><br>
  - <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C03/03-1.py">과제#3-1</a>에서 반지름을 입력받아 원의 둘레와 면적 구하기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C04/04-3.py">04-3.py</a><br>
</details>

<details>
<summary>과제05 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C05'>(Go)</a></summary>

  - 숫자를 입력받아, 구구단을 출력하는 gugudan(dan)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C05/05-1.py">05-1.py</a><br>
  - 섭씨를 화씨로 바꾸는 c2f(t_c)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C05/05-2.py">05-2.py</a><br>
  - 숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하는 sum_n(n)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C05/05-3.py">05-3.py</a><br>
</details>

<details>
<summary>과제06 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C06'>(Go)</a></summary>

  - 숫자 리스트를 받아 평균을 구하는 average(nums)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C06/H0601.py">H0601.py</a><br>
  - 1~n까지 리스트를 돌려주는 range_list(n)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C06/H0602.py">H0602.py</a><br>
  - 연도(y)를 주면, 윤년인지(True) 아닌지(False)알려주는 is_leap_year(y)함수 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C06/H0603.py">H0603.py</a>
    - 조건: 4로 나누었을때 나누어 떨어지면 윤년, 4로 나누어떨어지더라도 100으로 나누어 떨어진다면 윤년아님<br>
</details>

<details>
<summary>과제07 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C07'>(Go)</a></summary>

  - text2list(input_text), average(nums), median(nums)함수를 이용하여 아래 코드 실행되도록 제작 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C07/H07.py">H07.py</a><br>
  ```python
  def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums))) # 단, 갯수가 짝수일 경우 중앙에 위치한 두 값 중 큰 값 이용
  ```
</details>

<details>
<summary>과제08 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C08'>(Go)</a></summary>

  - 숫자가 여러줄에 걸쳐서 저장되있는 경우 각 숫자를 읽어와 아래 조건 출력 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C08/H08.py">H08.py</a><br>
      - 총 숫자의 개수
      - 주어진 숫자의 평균
      - 주어진 숫자의 최댓값
      - 주어진 숫자의 
</details>

<details>
<summary>과제09 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C09'>(Go)</a></summary>

  - 수업시간에 다룬 코드를 완성하고, 추가로 아래 질문에 답 출력 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C09/H09.py">H09.py</a><br>
      - 총 강수량: sum(rainfall) -> 함수 따로 만들지 않고 메인에서 값 확인
      - 강우일수: count_rain_days(rainfall)
      - 여름철(6~8월) 총 강수량: sumifs(rainfall, months, selected=[6, 7, 8])
      - 최장연속강우일수: longest_rain_days(rainfall)
      - 강우이벤트 중 최대 강수량: maximum_rainfall_event(rainfall)
      - 일교차가 가장 큰 날짜와 해당일자의 일교차(최고기온과 최저기온의 차이): maximum_temp_gap(dates, tmax, tmin) -> [2021, 1, 20], 23.2
      - 5월부터 9월까지의 적산온도(5도 이상의 온도 합): gdd(dates, tavg) -> 2050.5
</details>

<details>
<summary>과제10 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C10'>(Go)</a></summary>

  - 코드를 이용해 2020년 전주 측후소 주소를 다운받아 저장 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C10/H10.py">H10.py</a><br>
      - "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
      - 파일이 있는 경우 기존에 받은 파일을 이용
      - 결과는 화면에 출력하지 않고 파일에 저장
</details>

<details>
<summary>과제11 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C11'>(Go)</a></summary>

  - 관측이래 전주에서 가장 더웠던 날의 최고기온과 날짜, 가장 추웠을 때 최저기온과 날짜 구하기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C11/H11.py">H11.py</a><br>
      - "https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70"
      - 결과는 LMS참고 서버로 전송(hw11_submission.submit("홍길동", "2021-08-15", 40.1, "1978-01-04", -32.5))
</details>

<details>
<summary>과제12 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C12'>(Go)</a></summary>

  - 숫자를 입력받아 리스트 출력 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C12/H12.py">H12.py</a><br>
      - 숫자는 정수만 입력받고 자연수가 아닌 값은 무시
      - "-1"을 입력하면 입력을 더 이상 받지않고 현재까지 입력받은 값 출력
</details>

<details>
<summary>과제13 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C13'>(Go)</a></summary>

  - 구구단 문제를 제출하고, 정답 개수를 출력해 점수 출력 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C13/gugudan.py">gugudan.py</a><br>
      - random.randint(start, end)
  - 숨겨진 단어를 맞추는 행맨게임 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C13/hangman.py">hangman.py</a><br>
      - random.choice(list)
  - 로또번호 추출기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C13/lotto.py">lotto.py</a><br>
      - 1~45숫자 중 중복되지않게 6개 추출
</details>

<details>
<summary>중간고사 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C14'>(Go)</a></summary>

  - 2022년 3월 기준 연령별 남녀 인구분포표 그리기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C14/H14_population.py">H14_population.py</a><br>
      - Option1) 전북 전체, 전북 내 전체 시군구에 대한 그래프 저장
      - Option2) 지역을 사용자가 입력하면, 해당 지역의 그래프를 화면에 표시
  - 특정 날짜를 입력하면, 40년간 평균기온(1982-2021)의 그래프를 그리고, 해당 일자가 40년 기간 중 몇 번째 높은 기온인지 출력 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C14/H14_weather.py">H14_weather.py</a><br>
      - 2020년 5월 15일 선택시, 5월 15일 평균기온 그리기
      - 몇번째 높은 온도인지 표시하고, 그래프상에는 수평선을 그려서 강조하기
</details>

<details>
<summary>과제15 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C15'>(Go)</a></summary>

  - 도형 클래스 완성하기 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C15/H15_shape.py">H15_shape.py</a><br>
      - class Rectangle(Shape)
      - class Triangle(Shape)
      - class Circle(Shape)
      - class RegularHexagon(Shape)
      - 도전과제) 도형 클래스에 draw메소드를 추가하고 구현
  - 연령별 인구그래프를 클래스 형태로 변환 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C15/H15_population.py">H15_population.py</a><br>
</details>

<details>
<summary>과제16 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C16'>(Go)</a></summary>

  - ASCII코드를 이용해 입력받은 문자열 변환 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C16/H1601.py">H1601.py</a><br>
      - 대문자는 소문자로, 소문자는 대문자로
      - toggle_text(text:str) -> str
  - ASCII코드를 이용해 카이사르 암호 구현 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C16/H1602.py">H1602.py</a><br>
      - caesar_encode(text:str, shift:int =3) -> str
      - caesar_decode(text: str, shift:int =3) -> str
  - 유니코드를 이용한 초성게임 완성 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C16/H1603.py">H1603.py</a><br>
      - 주어진 단어 뭉치에서 단어를 하나 선택하고 초성 제시
      - 사용자는 주어진 초성을 보고 주어진 단어를 맞추는 게임
</details>

<details>
<summary>과제17 <a href='https://github.com/riverallzero/LEC_2022_programming/tree/main/%EA%B3%BC%EC%A0%9C17'>(Go)</a></summary>

  - GUI프로그램을 활용하여 카이사르 암호를 GUI로 구현 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C17/H1701.py">H1701.py</a><br>
  - 초성게임의 input()대신 gui_input()활용하여 구현 | <a href="https://github.com/riverallzero/LEC_2022_programming/blob/main/%EA%B3%BC%EC%A0%9C17/H1702.py">H1702.py</a><br>
</details>

<details>
<summary>기말고사 <a href='https://github.com/riverallzero/Personal_LmsNotion'>(Go)</a></summary>

  - LMS로 강의를 들을 때 놓치는 영상, 레포트, 퀴즈를 알려주기위한 알림 봇
</details>
