class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# для вставки (щоб створити дерево)
def insert(root, key):
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def find_max(root):
    """
    Знаходить найбільше значення у двійковому дереві пошуку.
    """
    # Перевірка на порожнє дерево
    if root is None:
        return None

    # Починаємо з кореня
    current = root

    # --> праворуч до упору
    # Поки існує правий нащадок, переходимо до нього
    while current.right is not None:
        current = current.right

    # значення найправішого вузла
    return current.key

def find_min(root):
    """
    Знаходить найменше значення у двійковому дереві пошуку.
    """
    # Перевірка на порожнє дерево
    if root is None:
        return None

    # Починаємо з кореня
    current = root

    # --> ліворуч до упору
    # Поки існує лівий нащадок, переходимо до нього
    while current.left is not None:
        current = current.left

    # значення найлівішого вузла
    return current.key

if __name__ == "__main__":

    root = Node(15)
    insert(root, 10)
    insert(root, 20)
    insert(root, 8)
    insert(root, 12)
    insert(root, 17)
    insert(root, 25) # найбільше значення

    # Візуально дерево виглядає так:
    #       15
    #      /  \
    #    10    20
    #   /  \   /  \
    #  8   12 17   25

    max_val = find_max(root)
    print(f"Найбільше значення в дереві: {max_val}")

    min_val = find_min(root)   
    print(f"Найменше значення в дереві: {min_val}") 
