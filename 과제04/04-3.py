import math

r = int(input('반지름: '))
pi = math.pi

l = 2*pi*r
s = pi*math.pow(r,2)

print('반지름이 {}인 원의 둘레는 {:.1f}, 원의 면적은 {:.2f}이다.' .format(r,l,s))
