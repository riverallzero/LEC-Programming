LEC Summary ZIP.
================

# 1. def main()함수 필수 요소
* def main():
    pass
* if __name__ == ' __main__ ':
    main()

- import할 때 def 함수():가 불러와지기 때문에 def main():의 내용은 상관 없음
*본인이 print하면서 확인하는 용도*

# 2. 모듈 필수 요소
* 빈 파일 생성
   __init__.py 

# 3. 파일 다운
* 기존 방식
f = open(filename)
lines = f.readlines()
* 추천 방식
with open(filename) as f:
    lines = f.readlines()
