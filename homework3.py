# normalization of phone numbers
import re

valid_numbers = [] # Список для валідних номерів
invalid_numbers = [] # Список для невалідних номерів

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "0-111-22-22",
    "00003850 111 22 11   ",
]

def normalize_phone(phone_number): # Функція для нормалізації номерів телефонів
    result_of_sub = re.sub(r'\D', '', phone_number) # Видаляємо всі нецифри
    if result_of_sub.startswith('380') and len(result_of_sub) == 12: # Перевірка на наявність коду країни та має 12 цифр
        return "+" + result_of_sub # Повертаємо номер з +
    if len(result_of_sub) == 9: # Перевірка на кількість цифр, якщо має 9 додаємо +380
        return "+380" + result_of_sub
    if result_of_sub.startswith('0') and len(result_of_sub) == 10: # Перевірка якщо номер починається на 0 та має 10 цифр
        return '+38' + result_of_sub # Якщо коду країни немає, додаємо +38

for num in raw_numbers: # Перебираємо всі номери
    normalized = normalize_phone(num)
    if normalized: # Перевірка на наявність номеру
        valid_numbers.append(normalized) # Додаємо валідний номер телефону в список valid_numbers
    else:
        invalid_numbers.append(num) # Додаємо невалідний номер телефону в список invalid_numbers


print("Невалідні номери телефонів:", invalid_numbers)
print("Валідні номери телефонів:", valid_numbers)

