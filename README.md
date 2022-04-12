LEC Summary ZIP.
================

### 1. def main()함수 필수 요소
* <pre><code> def main():
    pass    </code></pre>
* <pre><code> if __name__ == ' __main__ ':
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
<pre><code> f = open(filename)
lines = f.readlines() </code></pre>
* 추천 방식
<pre><code> with open(filename) as f:
    lines = f.readlines() </code></pre>
