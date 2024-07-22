def caching_fibonacci():
    # Створити порожній словник cache
    cache = {}

    def fibonacci(n):
        # Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
        # Якщо n == 1, повернути 1
        if n == 1:
            return 1
        # Якщо n вже є в cache, повернути значення з cache
        if cache.keys().__contains__(n):
            return cache[n]
        # Якщо число не знаходиться у кеші, обчислюємо його рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
