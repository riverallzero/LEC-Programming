import random

def read_input():
    return int(input('반복 횟수: '))

def main():
    score = 0

    for i in range(read_input()):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        answer = int(input('{} * {} = '.format(x, y)))

        if answer == x * y:
            score += 1
            print('정답')
        else:
            print('오답')
    print('정답 개수 {} 개' .format(score))


if __name__ == '__main__':
    main()