# FirstPhase / Day 3
# Экзамен из главы 5

# === Задача 1 ===
num = int(input())
if num % 100 == 0:
    print("YES")
else:
    print("NO")

# === Задача 2 ===
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 == b % 2 and c % 2 == d % 2 or a % 2 != b % 2 and c % 2 != d % 2:
    print("YES")
else:
    print("NO")

# === Задача 3 ===
age = int(input())
s = input()
if 10 <= age <= 15 and s == "f":
    print("YES")
else:
    print("NO")

# === Задача 4 ===
num = input()
if num == "1":
    print("I")
elif num == "2":
    print("II")
elif num == "3":
    print("III")
elif num == "4":
    print("IV")
elif num == "5":
    print("V")
elif num == "6":
    print("VI")
elif num == "7":
    print("VII")
elif num == "8":
    print("VIII")
elif num == "9":
    print("IX")
elif num == "10":
    print("X")
else:
    print("ошибка")

# === Задача 5 ===
num = int(input())
if num % 2 != 0:
    print("YES")
else:
    if 2 <= num <= 5:
        print("NO")
    elif 6 <= num <= 20:
        print("YES")
    else:
        print("NO")

# === Задача 6 ===
a = 4
b = 4
c = 5
d = 5
if (a - c) ** 2 == (b - d) ** 2:
    print("YES")
else:
    print("NO")

# === Задача 7 ===
a = int(input())
b = int(input())
c = int(input())
d = int(input())
dx = a - c
dy = b - d
if dx < 0:
    dx = -dx
if dy < 0:
    dy = -dy
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("YES")
else:
    print("NO")

# === Задача 8 ===
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((a - c) ** 2 == (b - d) ** 2) or (a == c or b == d):
    print("YES")
else:
    print("NO")
