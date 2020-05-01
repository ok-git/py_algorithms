"""
Закодируйте любую строку по алгоритму Хаффмана.
"""

import collections
from tree_model import Tree


def search_bst(root, number, path=''):
    if root.value == number:
        return f'{path}'
    if root.value > number and root.left is not None:
        return search_bst(root.left, number, path=f'{path}0')
    if root.value < number and root.right is not None:
        return search_bst(root.right, number, path=f'{path}1')
    return f'Число {number} отсутствует в дереве'


string = "beep boop beer!"
symbols_counter = collections.Counter(string)
# Counter({'e': 4, 'b': 3, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1})
# ----------------------------------------------------------------------------------------
#                                        Node[  8  ]
#                 Node[  4  ]                                 Node[ 12  ]
#      Node[  2  ]            Node[  6  ]          Node[ 10  ]            Node[ 14  ]
# Node[  0  ]Node[  3  ]Node[  5  ]Node[  7  ]Node[  9  ]Node[ 11  ]Node[ 13  ]Node[ 15  ]
# ----------------------------------------------------------------------------------------

t = Tree()
i = 0
while len(symbols_counter) > 1:
    pair = symbols_counter.most_common()[:-3:-1]
    key_1, val_1 = pair[0]
    key_2, val_2 = pair[1]
    symbols_counter.pop(key_1)
    symbols_counter.pop(key_2)
    t.root = t.new_node(i + 2)
    if type(key_1) == str and type(key_2) != str:
        key_1, key_2 = key_2, key_1
    if type(key_1) == str:
        t.root.left = t.new_node(i, key_1)
    else:
        t.root.left = key_1
    if type(key_2) == str:
        t.root.right = t.new_node(i + 1, key_2)
    else:
        t.root.right = key_2
    i += 3
    symbols_counter.update({t.root: val_1 + val_2})



# while len(symbols_counter) > 1:
#     key_1, val_1 = symbols_counter.popitem()
#     key_2, val_2 = symbols_counter.popitem()
#     node = HuffmanNode('')
#     node.left = HuffmanNode(key_1)
#     node.right = HuffmanNode(key_2)
#     symbols_counter[node] = val_1 + val_2

t.print_level_order(t.root)

#                                 Node[ 17  ]
#         Node[ 11  ]                                        Node[ 14  ]
# Node[  9  ]      Node[  8  ]                    Node[  5  ]            Node[ 13  ]
#           Node[  6  ]Node[  7  ]          Node[  2  ]     Node[  4  ]
#                                    Node[  0  ]   Node[  1  ]


print(symbols_counter)
print(search_bst(t.root, 0))
