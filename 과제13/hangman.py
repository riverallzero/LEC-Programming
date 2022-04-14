def main():
    answer = list(input('WORD: '))
    trial = int(input('시도: '))
    text = list('_'*len(answer))

    while trial > 0:
        print(text)
        letter = input('(남은 목숨 {}) 알파벳: ' .format(trial))
        if letter in answer:
            for i in range(len(answer)):
                if letter == answer[i]:
                    result = text[i] = letter
                    print(result)
        else:
            trial -= 1

        if '_' not in answer:
            break

    if trial > 0:
        print('정답')
    else:
        print('정답은 {} 입니다.' .format(answer))

if __name__ == '__main__':
    main()
