class Node:
    def __init__(self, value=None, left=None, right=None, data=""):
        self.value = value
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        return f"Node[{self.value:^2}-'{self.data}']"


class Tree:
    def __init__(self):
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, value, data=""):
        return Node(value, None, None, data)

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # функция для распечатки элементов на определенном уровне дерева с указнием пути к каждому узлу
    def print_given_level_with_path(self, root, level, path=''):
        if root is None:
            return
        if level == 1:
            print(root, f'({path})  ', end='\t')
        elif level > 1:
            self.print_given_level_with_path(root.left, level - 1,  f'{path}0')
            self.print_given_level_with_path(root.right, level - 1,  f'{path}1')

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1

    # функция для распечатки дерева с указнием пути к каждому узлу
    def print_level_order_with_path(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level_with_path(self.root, i)
            print()
            i += 1

    # моя адаптация функции для распечатки дерева на определенном уровне для получения кодов Хаффмана
    def get_huffman_codes_for_given_level(self, root, level, result, path=''):
        if root is None:
            return
        if level == 1:
            if root.left is None and root.right is None:
                return result.update({root.data: path})
        elif level > 1:
            self.get_huffman_codes_for_given_level(root.left, level - 1, result, f'{path}0')
            self.get_huffman_codes_for_given_level(root.right, level - 1, result,  f'{path}1')

    # моя адаптация функции для распечатки дерева для получения кодов Хаффмана
    def get_huffman_codes(self, root):
        result = {}
        h = self.height(root)
        i = 1
        while i <= h:
            self.get_huffman_codes_for_given_level(self.root, i, result)
            i += 1
        return result

    # функция для вычисления ширины дерева
    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1

        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)


if __name__ == '__main__':
    t = Tree()
    t.root = t.new_node(8)
    t.root.left = t.new_node(4)
    t.root.right = t.new_node(12)
    t.root.left.left = t.new_node(2)
    t.root.left.right = t.new_node(6)
    t.root.right.left = t.new_node(10)
    t.root.right.right = t.new_node(14)
    t.root.left.left.left = t.new_node(0)
    t.root.left.left.right = t.new_node(3)
    t.root.left.right.left = t.new_node(5)
    t.root.left.right.right = t.new_node(7)
    t.root.right.left.left = t.new_node(9)
    t.root.right.left.right = t.new_node(11)
    t.root.right.right.left = t.new_node(13)
    t.root.right.right.right = t.new_node(15)

    t.print_level_order(t.root)
    print(f'высота: {t.height(t.root)}')
    print(f'ширина: {t.get_max_width(t.root)}')
