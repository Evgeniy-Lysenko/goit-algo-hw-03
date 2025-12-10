# the number of days between a given date and a current date
from datetime import datetime
today_date = datetime.now() # Отримання поточнї дату
def get_valid_date(): # Перевірка введенної дати
    while True:
        input_date = input("Enter a date in the format YYYY-MM-DD: ")
        try:
            return datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

input_date = get_valid_date()


days = (today_date - input_date).days  
print(days)

