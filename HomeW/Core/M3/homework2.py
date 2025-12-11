# generation of a random number for lottery
import random
min = 0
max = 0
quantity = 0
def get_min_max_quantity(): 
    while True:
        min = int(input("Enter the minimum \>0: "))
        max = int(input("Enter the maximum quantity \<1000: "))
        quantity = int(input("Enter the quantity: "))
       
        if 0 < min <= (max - quantity) and max <=1000:
            return min, max, quantity
        else:   
            print("Invalid input. Please try again.") # Повідомлення про помилку



def get_numbers_ticket(min, max, quantity): # Генерація випадкового числа
   return [random.randint(min, max) for _ in range(quantity)]

min_value, max_value, quantity = get_min_max_quantity()
print(get_numbers_ticket(min_value, max_value, quantity))