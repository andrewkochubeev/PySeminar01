# Задача 2: Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число: "))
result = n % 10
n = n // 10
result += n % 10
n = n // 10
result += n % 10
print(result)