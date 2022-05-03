import random

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ',
                 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ',
                 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def main():
    wordlist = ['포도', '사과', '바나나', '키위', '딸기', '오렌지', '자몽', '레몬', '체리', '복숭아', '수박', '블루베리']
    choicelist = random.choice(wordlist)
    secret = choicelist
    answer = ['_' for i in range(len(secret))]
    trial = 5

    choseonglist = []
    for word in choicelist:
        if '가' <= word <= '힣':
            choseong = (ord(word) - ord('가')) // (21 * 28)
            choseonglist.append(CHOSUNG_LIST[choseong])

    while trial > 0:
        print('시도 {}) 과일 {} : ' .format(6-trial, choseonglist)+''.join(answer))
        letter = input('답안입력 = ')

        if letter in secret:
            for i in range(len(secret)):
                if letter == secret[i]:
                    answer[i] = letter
                    trial -= 1
        else:
            trial -= 1

        if '_' not in answer:
            break

    if trial > 0:
        print('{}, 정답!'.format(secret))

    else:
        print('오답! 정답은 {} 입니다.' .format(secret))

if __name__ == '__main__':
    main()