import re

def normalize_phone(phone_number):
    # нормалізує до стандартного формату, залишаючи тільки цифри та символ '+' на початку
    phone_number = re.sub(r'[^0-9+]', '', phone_number)
    
    # Якщо номер не містить міжнародного коду, функція автоматично додає код '+38'
    if phone_number.startswith('0'):
        phone_number = '+38' + phone_number[0:]
    # коли номер починається з '380' (додається лише '+'
    elif phone_number.startswith('380'):
        phone_number = '+' + phone_number[0:]
    
    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = [normalize_phone(number) for number in raw_numbers]

# Функція повертає нормалізований телефонний номер у вигляді рядка.
print("Нормалізовані номери телефонів для SMS-розсилки:", normalized_numbers)
