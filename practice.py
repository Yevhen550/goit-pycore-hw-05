# import collections

# Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# cat = Cat("Simon", 4, "Krabat")

# print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")


# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# print(mark_counts)

# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)


# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))

from collections import Counter

# # Створення Counter з рядка
# letter_count = Counter("banana")
# print(letter_count)

# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# print(words)
# word_count = Counter(words)

# # Виведення слова та його частоти
# for word, count in word_count.items():
#     print(f"{word}: {count}")

# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d["a"].append(1)
# d["a"].append(2)
# d["b"].append(4)

# print(d)


# words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

# from collections import defaultdict

# words = ["apple", "zoo", "lion", "lama", "bear", "bet", "wolf", "appendix"]
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))

# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append("a")
# queue.append("b")
# queue.append("c")

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append("middle")  # Додаємо 'middle' в кінець черги
# d.append("last")  # Додаємо 'last' в кінець черги
# d.appendleft("first")  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))

# from collections import deque

# d = deque(maxlen=3)
# for i in range(10):
#     d.append(i)

# print(d)


# from collections import deque

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"},
# ]

# Ініціалізація черги завдань
# task_queue = deque()

# Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")


# def my_generator():
#     yield 1
#     yield 2
#     yield 3


# gen = my_generator()

# # Використання next()
# print(gen)  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3

# !!!!===============================================================================


# from typing import Callable


# def add(a: int, b: int) -> int:
#     return a + b


# def multiply(a: int, b: int) -> int:
#     return a * b


# def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
#     return operation(a, b)


# # Використання
# result_add = apply_operation(5, 3, add)
# result_multiply = apply_operation(5, 3, multiply)

# print(result_add, result_multiply)


# def outer_function(msg):
#     message = msg

#     def inner_function():
#         print(message)

#     return inner_function


# # Створення замикання
# my_func = outer_function("Hello, world!")
# my_func()

from typing import Callable


def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count
        count += 1
        return count

    return increment


# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3
