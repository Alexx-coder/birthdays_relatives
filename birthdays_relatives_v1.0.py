import datetime
import time

print("Это напоминайка, здесь будут храниться даты рождений ваших родственников и будет писать через сколько времени у них др")
print("Впишите сюда родственников и их даты рождений")
print("Максимальное количество родственников - 8")

relative_1 = "Первый родственник"
print("\n",relative_1)
relative_1_name = input("Имя : ")
relative_1_br = input("Дата : ")

relative_2 = "Второй родственник"
print("\n",relative_2)
relative_2_name = input("Имя : ")
relative_2_br = input("Дата : ")

relative_3 = "Третий родственник"
print("\n",relative_3)
relative_3_name = input("Имя : ")
relative_3_br = input("Дата : ")

relative_4 = "Четвёртый родственник"
print("\n",relative_4)
relative_4_name = input("Имя : ")
relative_4_br = input("Дата : ")

relative_5 = "Пятый родственник"
print("\n",relative_5)
relative_5_name = input("Имя : ")
relative_5_br = input("Дата : ")

relative_6 = "Шестой родственник"
print("\n",relative_6)
relative_6_name = input("Имя : ")
relative_6_br = input("Дата : ")

relative_7 = "Седьмой родственник"
print("\n",relative_7)
relative_7_name = input("Имя : ")
relative_7_br = input("Дата : ")

relative_8 = "Восьмой родственник"
print("\n",relative_8)
relative_8_name = input("Имя : ")
relative_8_br = input("Дата : ")

relatives_all = (
    f"{relative_1_name}: {relative_1_br}",
    f"{relative_2_name}: {relative_2_br}",
    f"{relative_3_name}: {relative_3_br}",
    f"{relative_4_name}: {relative_4_br}",
    f"{relative_5_name}: {relative_5_br}",
    f"{relative_6_name}: {relative_6_br}",
    f"{relative_7_name}: {relative_7_br}",
    f"{relative_8_name}: {relative_8_br}"
)


time_now = datetime.datetime.now()
year_now = time_now.year
month_now = time_now.month
day_now = time_now.day
hour_now = time_now.hour
minute_now = time_now.minute
second_now = time_now.second


print("Выберете родственника")

for i,relative in enumerate(relatives_all, 1):
    print(f"{i}. {relative}") 


while True:
    try:
        choice = int(input("\nВведите нужного вам родственника"))
        if 1 <= choice <= 8:
            break
        else:
            print("Такого родственника нет.\nВведите число от 1 до 8")
    except ValueError:
        print("Введите число от 1 до 8")

print("Вы выбрали: {relatives_all[choice_1]}")


print("\n")
print("Аналитика информации для; {relatives_all[choice-1]}")


chosen_relative_index = choice - 1
relative_info = relatives_all[chosen_relative_index]


try:
    name_part, date_part = relative_info.split(":", 1)
    date_str = date_part.strip()  
    
    if len(date_str.split('.')) == 2:
        day, month = map(int, date_str.split('.'))
        birthday = datetime.datetime(year_now, month, day)
    else:
        day, month, year = map(int, date_str.split('.'))
        birthday = datetime.datetime(year, month, day)
    
    next_birthday = datetime.datetime(year_now, birthday.month, birthday.day)
    if next_birthday < time_now:
        next_birthday = datetime.datetime(year_now + 1, birthday.month, birthday.day)
    
    time_left = next_birthday - time_now

    print(f"Следующий день рождения: {next_birthday.strftime('%d.%m.%Y')}")
    print(f"Осталось: {time_left.days} дней")

    if time_left.days == 0:
        print("СЕГОДНЯ ДЕНЬ РОЖДЕНИЯ! ПОЗДРАВЬ РОДСТВЕННИКА!")
    elif time_left.days < 30:
        print("Уже скоро! Приготовь подарок ко дню рождению родственника!")

            
except (ValueError, IndexError):
    print(f"Не удалось найти дату: '{date_str}'")
    print("Пожалуйста, введите дату в формате 'дд.мм.гггг' или 'дд.мм'")

print("\n")
print("Текущая дата и время:")
print(f"Дата : {day_now:02}.{month_now:02}.{year_now}")
print(f"Время : {hour_now:02}:{minute_now:02}:{second_now:02}")

#Данный проект и версия проекта написана Alexx-coder или alex
#Проект лицензирован под MIT LICENSE-см.файл LICENSE
