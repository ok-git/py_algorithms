"""
Блок-схема https://drive.google.com/open?id=1yQHtcE4Ho_IYLYJ2ChF1zoPMsuAkqdg8
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = int(input("Введите трёхзначное число: "))

d1 = number // 100
d2 = number % 100 // 10
d3 = number % 100 % 10
sum_res = d1 + d2 + d3
multiply_res = d1 * d2 * d3

print(f"Сумма цифр {sum_res}, произведение цифр - {multiply_res} ")
