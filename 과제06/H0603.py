# def is_leap_year(y):
#     if y % 4 == 0:
#         if y % 100 == 0:
#             return False
#         else:
#             return True
#     else:
#         return False
    
# def main():
#     y = int(input('연도: '))
#     if is_leap_year(y):
#         print('윤년이 맞습니다.')
#     else:
#         print('윤년이 아닙니다.')
        
# if __name__ == '__main__':
#     main()

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False

def main():
    y = int(input('연도: '))
    print(is_leap_year(y))
    if is_leap_year(y):
        print('윤년이 맞습니다.')
    else:
        print('윤년이 아닙니다.')

if __name__ == '__main__':
    main()
