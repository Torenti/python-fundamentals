# FirstPhase / Day 3
# Задачи из главы 4_2

# === Задача 1 ===
if -1 < int(input()) < 17:
    print("Принадлежит")
else:
    print("Не принадлежит")

# === Задача 2 ===
num = int(input())
if num <= -3 or num >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")

# === Задача 3 ===
num = int(input())
if num > -30 and num <= -2 or num > 7 and num <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")

# === Задача 4 ===
num = int(input())
if num > 999 and num < 10000 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")

# === Задача 4 ===
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# === Задача 5 ===
num = int(input())
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("YES")
else:
    print("NO")

# === Задача 6 ===
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if a1 == b1 or a2 == b2:
    print("YES")
else:
    print("NO")

# === Задача 7 ===
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if (a1 - b1 <= 1 and b1 - a1 <= 1 and a2 - b2 <= 1 and b2 - a2 <= 1) and (
    a1 - b1 >= -1 and b1 - a1 >= -1 and a2 - b2 >= -1 and b2 - a2 >= -1
):
    print("YES")
else:
    print("NO")
