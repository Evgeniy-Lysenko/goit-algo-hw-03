# generation of a random number for lottery
import random
def get_min_max_quantity(): # Функція для отримання даних з користувача та перевірки введених даних
    while True:
        min_value = int(input(f"Enter the minimum from 1 to 1000: "))
        max_value = int(input(f"Enter the maximum from {(min_value+1)} to 1000: "))
        quantity = int(input(f"Enter the quantity of numbers from 1 to {(max_value - min_value + 1)}: "))
       
        if 0 < min_value < max_value and max_value < 1001 and 0 < quantity <= (max_value - min_value + 1): # Перевірка коректності введених даних
            return min_value, max_value, quantity
        else:   
            print("Invalid input. Please try again.") # Повідомлення про помилку



def get_numbers_ticket(min, max, quantity): # Генерація випадкового числа
    return random.sample(range(min, max + 1), quantity)

min, max, quantity = get_min_max_quantity() # Виклик функції для отримання даних з користувача
print("Ваші лотерейні числа:", get_numbers_ticket(min, max, quantity)) # Вивід варіантів випадкових чисел для лотереї по заданим користувачем параметрам 