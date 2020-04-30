"""
Закодируйте любую строку по алгоритму Хаффмана.
"""
import collections
from tree_model import Tree
from tree_model import Node

class HuffmanNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # return f'Node[{self.value:^5}]'
        return f"Node {self.value} - left {self.left} - right {self.right}"

    def __str__(self):
        return f"{self.value} - {self.left} - {self.right}"


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
while len(symbols_counter) > 1:
    key_1, val_1 = symbols_counter.popitem()
    key_2, val_2 = symbols_counter.popitem()
    t.root = t.new_node(val_1 + val_2)
    t.root.left = t.new_node(key_1)
    t.root.right = t.new_node(key_2)
    symbols_counter.update({t.root: val_1 + val_2})
    # symbols_counter[t.root] = val_1 + val_2

# while len(symbols_counter) > 1:
#     key_1, val_1 = symbols_counter.popitem()
#     key_2, val_2 = symbols_counter.popitem()
#     node = HuffmanNode('')
#     node.left = HuffmanNode(key_1)
#     node.right = HuffmanNode(key_2)
#     symbols_counter[node] = val_1 + val_2

t.print_level_order(t.root)

print(symbols_counter)
print(len(symbols_counter))
