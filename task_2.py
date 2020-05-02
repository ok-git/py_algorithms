"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import collections
from tree_model import Tree

string = "beep boop beer!"
symbols_counter = collections.Counter(string)
print(f"\nИсходная строка: {string}")
print(f"Частоты всех символов: {symbols_counter}\n")
# Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})

t = Tree()  # Создаём дерево - использую код из методички, что бы не изобритать велосипед
i = 0  # Счётчик узлов дерева - в алгоритме не нужен, использую для более наглядной визуализации и отладки
while len(symbols_counter) > 1:
    pair = symbols_counter.most_common()[:-3:-1]  # берём пару наименее частых объектов
    obj_1, counter_1 = pair[0]  # взяли первый объект и его счётчик частот
    obj_2, counter_2 = pair[1]  # взяли второй объект и его счётчик частот
    symbols_counter.pop(obj_1)  # удалили первый объект из Counter (почему-то popitem работает как-то странно)
    symbols_counter.pop(obj_2)  # удалили второй объект из Counter
    t.root = t.new_node(i + 2)  # создали верхний (корневой) узел дерева
    if type(obj_1) == str:  # если объект это строка, то создаем новый узел (слева от корня) и помещаем объект в data
        t.root.left = t.new_node(i, obj_1)
    else:
        t.root.left = obj_1  # иначе, объект - это уже узел дерева и тогда "подклеиваем" его в левое ребро
    if type(obj_2) == str:  # если объект это строка, то создаем новый узел (справа от корня) и помещаем объект в data
        t.root.right = t.new_node(i + 1, obj_2)
    else:
        t.root.right = obj_2  # иначе, объект - это уже узел дерева и тогда "подклеиваем" его в правое ребро
    i += 3  # увеличиваем счётчик узлов дерева
    symbols_counter.update({t.root: counter_1 + counter_2})  # возвращаем созданное дерево в Counter, частоты суммируем

t.print_level_order_with_path(t.root)  # Распечатаем дерево с указанием пути до каждого узла, в скобках

#                 /----------------------- Node[17-''] () -----------------------------\
#         Node[11-''] (0)                                                            Node[14-''] (1)
#        /                \                                                        /                 \
# Node[9 -'b'] (00)      Node[8 -''] (01)                              Node[5 -''] (10)              Node[13-'e'] (11)
#                            /         \                              /               \
#                Node[6 -' '] (010)   Node[7 -'p'] (011)      Node[2 -''] (100)       Node[4 -'o'] (101)
#                                                                /          \
#                                                  Node[0 -'!'] (1000)   Node[1 -'r'] (1001)

huffman_codes = t.get_huffman_codes(t.root)
print('\nТаблица с кодами Хаффмана для символов из исходной строки: ')
for key, val in huffman_codes.items():
    print(f'{key} - {val}')

coded_string = "".join(huffman_codes[symbol] for symbol in string)
print(f"\nЗакодированная строка:\n{coded_string}")
