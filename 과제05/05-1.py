def gugudan(dan):
        
    print('[ {}단의 구구단 ]' .format(dan))

    for i in range(1, 10):
        print(dan, '*', i, '=', dan*i)

if __name__ == '__main__':
    dan = int(input('단: '))
    gugudan(dan)
