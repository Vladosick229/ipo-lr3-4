num1 = float(input("Введите первое число: "))# ввод первого числа
num2 = float(input("Введите второе число: "))# ввод второго числа
num3 = float(input("Введите третье число: "))# ввод третьего числа

if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(f"Наибольшее число: {largest}") # вывод результата
