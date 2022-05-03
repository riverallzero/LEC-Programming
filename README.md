LEC Summary ZIP.
================

### 1. def main()함수 필수 요소
<pre><code>def main():
    return    </code></pre>
<pre><code>if __name__ == ' __main__ ':
    main() </code></pre>

> import할 때 def 함수():가 불러와지기 때문에 def main():의 내용은 상관 없음   
>   > 본인이 print하면서 **확인하는 용도**

***

### 2. 모듈 필수 요소
빈 파일 생성
<pre><code>__init__.py</code></pre>
  
***

### 3. 파일 다운
* 기존 방식
<pre><code>f = open(filename)
lines = f.readlines() </code></pre>
* 추천 방식
<pre><code>with open(filename) as f:
    lines = f.readlines() </code></pre>
* 다운 경로
<pre><code>if not os.path.exists(filename):
        res = requests.get(URL)</code></pre>

***

### 4. CLASS
*  def  함수 이름 count_rainfall()
* class 함수 이름 CountRainfall
* <pre><code>def 메서드(self):</code></pre> 여기서 self는 키워드. 다른 변수로 바꾸면 안됨(ex. self = 3 불가)

* class 안에 들어있는 함수는 메서드
* 특수 메서드로 편리하게 사용 가능
<pre><code>if querry == 'v':
    print(r.v)
elif querry =='h':
    print(r.h) </code></pre>
<pre><code>= print(getattr(r, querry))</code></pre>

***

### 5. ASCII &  UNICODE
* ACII : 소문자 = 대문자 + 32
