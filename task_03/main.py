# Трохи вийшов за рамки завдання, зробив просте меню для взаємодії з деревом.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.key

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key

def get_sum(root):
    if root is None:
        return 0
    # Рекурсивно: значення поточного + сума зліва + сума справа
    return root.key + get_sum(root.left) + get_sum(root.right)


def print_tree(root, space=0, level_gap=5):
    """
    Вивести дерево в звичному вигляді чуть не вийшло :(
    Зробив, повертаючи його на 90 градусів.
    Корінь буде зліва.
    """
    if root is None:
        return

    space += level_gap

    # Спочатку правепіддерево (зверху)
    print_tree(root.right, space)

    # Поточний вузол
    print() 
    for i in range(level_gap, space):
        print(end=" ")
    print(f"{root.key}")

    # Потім ліве піддерево (знизу)
    print_tree(root.left, space)


if __name__ == "__main__":
    root = Node(15)
    keys_to_add = [10, 20, 8, 12, 17, 25, 5, 30]
    
    print("Наповнюємо дерево...")
    for key in keys_to_add:
        insert(root, key)
    
    while True:
        print("\n" + "="*30                         )
        print("МЕНЮ КЕРУВАННЯ ДЕРЕВОМ"              )
        print("="*30                                )
        print("1. Показати дерево (Візуалізація)"   )
        print("2. Знайти мінімум (Min)"             )
        print("3. Знайти максимум (Max)"            )
        print("4. Знайти суму (Sum)"                )
        print("5. Вихід"                            )
        
        choice = input("\nВаш вибір: ")

        if choice == '1':
            print("\Структура дерева (повернуто вліво):")
            print_tree(root)
        elif choice == '2':
            print(f"--> Найменше значення: {find_min(root)}")
        elif choice == '3':
            print(f"--> Найбільше значення: {find_max(root)}")
        elif choice == '4':
            print(f"--> Сума всіх значень: {get_sum(root)}")
        elif choice == '5':
            print("Дякую за роботу!")
            break
        else:
            print("Невірний вибір.")