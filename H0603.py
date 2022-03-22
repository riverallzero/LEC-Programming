def is_leap_year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return 'True'
    else:
        return 'False'

def main():
    y = int(input('연도: '))
    print('{} 년 윤년 여부 = {}' .format(y, is_leap_year(y)))

if __name__ == '__main__':
    main()