"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

MIN_ITEM = 2
MAX_ITEM = 100
array = [i for i in range(MIN_ITEM, MAX_ITEM)]
result = [0] * 10

for el in array:
    for denominator in range(2, 10):
        if el % denominator == 0:
            result[denominator] += 1

print("Количество кратных чисел, из исходного массива:")
for i in range(2, 10):
    print(f"{i} - {result[i]}")
