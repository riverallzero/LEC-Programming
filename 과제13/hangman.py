def read_input():
    return input('알파벳 입력: ')

def main():
    answer = 'apple'
    trial = 5
    answer_list = list(answer)
    text = list('_____')
    print(text)

    for i in range(trial):
        if read_input() == answer_list[0]:
            print(text[0].replace('_', read_input()))
        elif read_input() == answer_list[1]:
            print(text[1].replace('_', read_input()))
        elif read_input() == answer_list[2]:
            print(text[2].replace('_', read_input()))
        elif read_input() == answer_list[3]:
            print(text[3].replace('_', read_input()))
        elif read_input() == answer_list[4]:
            print(text[4].replace('_', read_input()))
        else:
            print('정답은 {} 입니다.' .format(answer))

if __name__ == '__main__':
    main()