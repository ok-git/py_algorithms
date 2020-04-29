"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:
func("papa")
6
func("sova")
9
"""


def hash_subs(string):
    result = set()
    for chunk in range(1, len(string)):
        for i in range(len(string)):
            result.add(hash(string[i:i + chunk]))
    return len(result)


print(hash_subs("sova"))  # 9
print(hash_subs("papa"))  # 6
