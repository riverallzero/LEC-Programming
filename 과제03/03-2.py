h = int(input('한라봉 섭취량(g): '))
s = int(input('딸기 섭취량(g): '))
b = int(input('바나나 섭취량(g): '))

kcal_h = h*(49/100)
kcal_s = s*(35/100)
kcal_b = b*(80/100)

print('한라봉 {}kcal/100g' .format(kcal_h))
print('딸기 {}kcal/100g' .format(kcal_s))
print('바나나 {}kcal/100g' .format(kcal_b))
