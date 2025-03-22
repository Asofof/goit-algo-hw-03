import random

def get_numbers_ticket(min, max, quantity):

    # Перевіряємо, що вхідні параметри відповідають заданим обмеженням.
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return [] # возвращает пустой список
    
    # Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
    unique_numbers = random.sample(range(min, max + 1), quantity)

    # Функція повертає відсортований список унікальних чисел.
    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)