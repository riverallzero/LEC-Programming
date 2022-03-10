import math
x1 = int(input('X1: '))
x2 = int(input('X2: '))
y1 = int(input('Y1: '))
y2 = int(input('Y2: '))

l = math.sqrt((x2-x1)**2+(y2-y1)**2)

print('두 지점 사이의 거리는 {}입니다.' .format(l))
