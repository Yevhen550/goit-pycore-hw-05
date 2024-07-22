import re
from typing import Callable


def generator_numbers(text: str):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел.
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        # Повертаємо дійсне число як результат.
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total = sum(func(text))  # Викликаємо generator_numbers.
    return total


text = "Загальний дохід працівника складається з декількох частин: \
        1000.01 як основний дохід, доповнений додатковими \
        надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# ? Очікуване виведення: Загальний дохід: 1351.46
