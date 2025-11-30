
# # Using the datetime module to get current date and time
# import datetime
# now = datetime.datetime.now()
# print(now)

#  Alternative approach
# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute) # 
# print(current_datetime.second) # 
# print(current_datetime.microsecond) #
# print(current_datetime.tzinfo) # prints None if no timezone is set
# print(current_datetime) # prints the full datetime object


# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())
# print(current_datetime.strftime("%Y-%m-%d %H:%M:%S")) # Formatted date and time
# print(current_datetime.isoformat()) # ISO 8601 format
# print(current_datetime.weekday()) # Day of the week as an integer (0=Monday, 6=Sunday)
# print(current_datetime.ctime()) # Human-readable string representation  of the date and time
# print(current_datetime.timestamp()) # Unix timestamp
# print(current_datetime.utcoffset()) # UTC offset, None if no timezone is set
# print(current_datetime.replace(year=2025)) # Replace year with 2025    


# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime   
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"
# print(type(time_part))



# from datetime import datetime, timedelta
# # Поточний час
# now = datetime.now()
# print("Поточний час:", now) 
# hour = now.hour
# minute = now.minute
# second = now.second
# print(f"Години: {hour}, Хвилини: {minute}, Секунди: {second}")

# day_now = datetime.date(now)
# print("Поточна дата:", day_now)
# print(f"Рік: {day_now.year}, Місяць: {day_now.month}, День: {day_now.day}")
# print("День тижня (0-Понеділок, 6-Неділя):", (day_now.weekday() +1))
# print("День року:", day_now.timetuple().tm_yday)
# print("Чи є високосним рік?:", day_now.year % 4 == 0 and (day_now.year % 100 != 0 or day_now.year % 400 == 0))
# print("Кількість днів у місяці:", (datetime(now.year, now.month % 12 + 1, 1) - timedelta(days=1)).day)
# print("Часова зона:", now.tzinfo)
# print
# # Дата і час через 5 днів
# future_date = now + timedelta(days=5)
# print("Дата і час через 5 днів:", future_date)  
# # Дата і час 3 дні тому
# past_date = now - timedelta(days=3)
# print("Дата і час 3 дні тому:", past_date)  
# # Різниця між двома датами
# date1 = datetime(2023, 12, 20)
# date2 = datetime(2023, 12, 14)
# difference = date1 - date2


# import datetime

# day_now = datetime.datetime.now()
# days = ["Понеділок","Вівторок","Середа","Четвер","П’ятниця","Субота","Неділя"]

# day_number = day_now.weekday() + 1   # 1–Понеділок, 7–Неділя
# day_name = days[day_now.weekday()]

# print(f"Сьогодні {day_number}-й день тижня: {day_name}")
# # print(f"Сьогодні {day_now.isoweekday()}-й день тижня: {days[day_now.isoweekday()-1]}")

# days[5] = "Ехху Субота!"
# print(days)

# day_name = days[day_now.weekday()]
# print(f"Сьогодні {day_number}-й день тижня: {day_name}")

# import datetime

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7)

# print(specific_date)  # Виведе "2020-01-07 00:00:00"

# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
# print(date_part)
# print(time_part)
# date_part2 = datetime.datetime(2023, 12, 14, 12, 30, 15)
# print(date_part2)

# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 7, 12, 3, 3)
# datetime2 = datetime(2023, 3, 15, 3, 5, 8)
# print(datetime1, datetime2)


# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# # Різниця між двома датами
# difference = datetime2 - datetime1
# print(difference)  #    Виведе "8 days, 0:02:05"   
# print(difference.days)  #  Виведе 8
# print(difference.seconds)  # Виведе 125 (кількість секунд понад повні дні)    
# print(difference.total_seconds())  #  Виведе 691205.0 (загальна кількість секунд у різниці)  
# print((difference.total_seconds()/60)/60)  #   Виведе 191.44583333333333 (загальна кількість годин у різниці)


# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)
# print("Дні:", delta.days)
# print("Секунди:", delta.seconds)
# print("Мікросекунди:", delta.microseconds)
# print("Загальна кількість секунд:", delta.total_seconds())  

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0
# print(difference.days)  # 365   

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)
# future_date = now - timedelta(days=10)  # Віднімаємо 10 днів від поточної дати
# print(future_date)  

from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

