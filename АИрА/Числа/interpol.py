class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)

def binary_tree_search(root, value, count):
    if root is None or root.value == value:
        if root is None:
            return -1, count
        else:
            return root, count
    count += 1
    if root.value < value:
        return binary_tree_search(root.right, value, count)
    return binary_tree_search(root.left, value, count)

lst = [1, 2, 3, 4, 5, 8, 9, 11]
elm = 8

root = Node(lst[0])
for i in range(1, len(lst)):
    insert_node(root, Node(lst[i]))

result, steps = binary_tree_search(root, elm, 0)

if result == -1:
    print("Число не найдено")
else:
    print(f"Число найдено на позиции {steps} с количеством шагов {steps}")