"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод
выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def rec_code_chr(start, stop):
    if start == stop:
        return f"{str(start)} - {chr(start)}"
    else:
        return f"{str(start)} - {chr(start)} {rec_code_chr(start + 1, stop)}"


first = 32
last = 127
step = 10

for i in range(first, last, step):
    print(rec_code_chr(i, i + 9 if i + 9 < last else last))
