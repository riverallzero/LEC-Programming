def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            return False
        elif y % 100 != 0:
            return True
        else:
            return False
    else:
        return False
    
def main():
    y = int(input('연도: '))
    print('{} 년 윤년 여부 = {}' .format(y, is_leap_year(y)))

if __name__ == '__main__':
    main()
