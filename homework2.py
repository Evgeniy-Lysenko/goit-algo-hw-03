# generation of a random number for lottery
import random

def get_numbers_ticket(min, max, quantity): # Генерація випадкового числа
    
    if 0 < min <= max and max < 1001 and 0 < quantity <= (max - min + 1): # Перевірка коректності введених даних
        return sorted(random.sample(range(min, max + 1), quantity)) # Генерація випадкового числа для лотереї 

    else:   
        return []
    
min = int(input(f"Enter the minimum from 1 to 1000: ")) # Введення мінімального значення
max = int(input(f"Enter the maximum from {(min)} to 1000: ")) # Введення максимального значення
quantity = int(input(f"Enter the quantity of numbers from 1 to {(max - min + 1)}: ")) # Введення кількості випадкових чисел

print("Ваші лотерейні числа:", get_numbers_ticket(min, max, quantity)) #  Виведення отсортованих випадкових чисел для лотереї 