# Імпортуйте модуль datetime
from datetime import datetime 

def get_days_from_today(date: str) -> int:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД'. Возвращает целое число
    
    try:
        # Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
        datetime_object = datetime.strptime(date, "%Y-%m-%d")

        # Отримайте поточну дату, використовуючи datetime.today().
        current_datetime = datetime.today()

        # Розрахуйте різницю між поточною датою та заданою датою.
        difference = current_datetime - datetime_object

        # Поверніть різницю у днях як ціле число.
        return difference.days
    except(ValueError):
        return "Неправильний формат вхідних даних."

print(get_days_from_today("2028-10.10"))


