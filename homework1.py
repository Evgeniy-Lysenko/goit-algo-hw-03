# the number of days between a given date and a current date
from datetime import datetime
today_date = datetime.now() # Отримання поточнї дату
def get_valid_date(): # Перевірка введенної дати
    while True:
        input_date = input("Enter a date in the format YYYY-MM-DD: ")
        try:
            return datetime.strptime(input_date, "%Y-%m-%d") # Перевірка формату дати
        except ValueError:
            print("Invalid date format. Please try again.") # Повідомлення про помилку при неправильному форматі дати

input_date = get_valid_date()

def get_days_from_today(date): # Розрахунок кількості днів між двома датами
    return (today_date - date).days
 
print(get_days_from_today(input_date)) # Вивід кількості днів між двома датами

