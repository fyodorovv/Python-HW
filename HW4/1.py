# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10 ^ {-1} ≤ d ≤10 ^ {-10}$

from math import pi

num_pi = int(input("Введите число: "))
print(f'Число Пи с заданной точностью {round(pi, num_pi)}')
