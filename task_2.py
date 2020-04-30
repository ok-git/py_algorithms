"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
import collections

string = "beep boop beer!"

symbols_counter = collections.Counter(string)

print(symbols_counter)