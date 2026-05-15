# FirstPhase / Day 3
# Задачи из главы 4_1

# === Задача 1 ===
password = input()
password_repeat = input()
if password == password_repeat:
    print("Пароль принят")
else:
    print("Пароль не принят")

# === Задача 2 ===
if int(input()) % 2 == 0:
    print("Четное")
else:
    print("Нечетное")

# === Задача 3 ===
if int(input()) >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# === Задача 4 ===
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)

# === Задача 5 ===
a = int(input())
b = int(input())
c = int(input())
if (b - a) == (c - b):
    print("YES")
else:
    print("NO")

# === Задача 6 ===
num = int(input())
first = num // 1000
last = num % 10
second = num // 100 % 10
third = num // 10 % 10
if (first + last) == (second - third):
    print("ДА")
else:
    print("НЕТ")

# === Задача 7 ===
sum = 0
a = int(input())
b = int(input())
c = int(input())
if a > 0:
    sum = sum + a
if b > 0:
    sum = sum + b
if c > 0:
    sum = sum + c
print(sum)

# === Задача 8 ===
age = int(input())
if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if age >= 60:
    print("старость")

# === Задача 9 ===
minnum = int(input())
b = int(input())
c = int(input())
d = int(input())
if minnum > b:
    minnum = b
if minnum > c:
    minnum = c
if minnum > d:
    minnum = d
print(minnum)
