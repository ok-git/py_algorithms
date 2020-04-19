"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

avg_profit_for_all = 0
sum_profit_for_all = 0
companies_dict = defaultdict(list)
for i in range(int(input('Количество предприятий: '))):
    entry = companies_dict[input(f'Название {i + 1}-го предприятия: ')]
    entry.extend(map(float, input('Прибыль за 4 квартала (через пробел): ').split()))
    entry.extend([sum(entry) / len(entry)])
    sum_profit_for_all += entry[-1]
avg_profit_for_all = sum_profit_for_all / len(companies_dict.keys())

print(f'Средняя прибыль по всем предприятиям: {avg_profit_for_all:.2f}')

print('Предприятия, чья прибыль выше среднего: ')
for company, profits in companies_dict.items():
    if profits[-1] >= avg_profit_for_all:
        print(f'{company}, средняя прибыль {profits[-1]}')

print('Предприятия, чья прибыль меньше среднего: ')
for company, profits in companies_dict.items():
    if profits[-1] < avg_profit_for_all:
        print(f'{company}, средняя прибыль {profits[-1]}')
