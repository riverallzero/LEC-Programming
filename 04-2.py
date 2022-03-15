h = int(input('한라봉 섭취량(g): '))
s = int(input('딸기 섭취량(g): '))
b = int(input('바나나 섭취량(g): '))

cal = {'한라봉':49, '딸기':35, '바나나':80}

kcal_h = h*(cal['한라봉']/100)
kcal_s = s*(cal['딸기']/100)
kcal_b = b*(cal['바나나']/100)

print('한라봉 {}kcal/100g' .format(kcal_h))
print('딸기 {}kcal/100g' .format(kcal_s))
print('바나나 {}kcal/100g' .format(kcal_b))
