x = int(input('X= '))
y = int(input('y= '))

if int(x) > 0 and int(y) > 0:
    print('입력한 좌표는 1사분면입니다.')

elif int(x) < 0 and int(y) > 0:
    print('입력한 좌표는 2사분면입니다.')

elif int(x) < 0 and int(y) < 0:
    print('입력한 좌표는 3사분면입니다.')

else:
    print('입력한 좌표는 4사분면입니다.')
