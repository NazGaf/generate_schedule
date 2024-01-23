"""
from datetime import datetime, timedelta - Цей рядок імпортує 
з модуля datetime класи datetime 
та timedelta. datetime дозволяє працювати з датами і часом, а 
timedelta дозволяє працювати з проміжками часу.

def generate_schedule(days, work_days, rest_days, start_date): - 
Це визначення функції generate_schedule, яка приймає чотири аргументи: 
days (кількість днів), work_days (кількість робочих днів), 
rest_days (кількість днів відпочинку) та start_date.

schedule = [] – це створення порожнього списку schedule, який буде 
використовуватись для зберігання розкладу робочих днів.

current_date = start_date - Це надання змінної current_date початкової дати.

for i in range(days): - Це початок циклу, який виконуватиметься days разів.

if i % (work_days + rest_days) < work_days: - Це умова, яка перевіряє, 
чи поточний день є робочим або вихідним. Оператор % повертає залишок 
від розподілу, тому i % (work_days + rest_days) дає послідовність робочих 
та вихідних днів. Якщо залишок менший за work_days, це означає, 
що поточний день є робочим.

schedule.append(current_date) - Якщо поточний день є робочим, 
ми додаємо його до розкладу.

current_date += timedelta(days=1) - Після додавання поточної 
дати до розкладу або після переходу на наступний день, ми збільшуємо поточну 
дату на один день за допомогою timedelta(days=1).

return schedule - Після завершення циклу ми повертаємо отриманий розклад.
"""

from datetime import datetime, timedelta

def generate_schedule(days, work_days, rest_days, start_date):
    
    schedule = []
    
    current_date = start_date
    
    for i in range(days):
        
        if i % (work_days + rest_days) < work_days:
            
            schedule.append(current_date)
            
        current_date += timedelta(days=1)
        
    return schedule

# Тести

print(generate_schedule(5, 2, 1, datetime(2020, 1, 30)))