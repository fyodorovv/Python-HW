# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

fourth = int(input("Введите номер четверти"))

if fourth == 1:
    print("X = больше нуля, Y больше нуля")
elif fourth == 2:
    print("X = меньше нуля, Y больше нуля")
elif fourth == 3:
    print("X = меньше нуля, Y меньше нуля")
elif fourth == 4:
    print("X = больше нуля, Y меньше нуля")
else:
    print("Ошибка")