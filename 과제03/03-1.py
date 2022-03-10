from cmath import sqrt
import math

r = int(input('반지름: '))
pi = math.pi
s = pi*math.pow(r,2)

print('반지름 {}에 대한 원의 면적은 {}이다.' .format(r,s))
