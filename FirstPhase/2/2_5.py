# FirstPhase / Day 2
# Задачи из главы 2.5

# === Задача 1 ===
b = int(input())
q = int(input())
n = int(input())
print(b * q ** (n - 1))

# === Задача 2 ===
print(int(input()) // 100)

# === Задача 3 ===
n = int(input())
k = int(input())
print(k // n, "\n", k % n, sep="")

# === Задача 4 ===
naselenie = int(input())
print(naselenie // 2 + naselenie % 2)

# === Задача 5 ===
minut = int(input())
print(minut, "мин - это", minut // 60, "час", minut % 60, "минут.")

# === Задача 6 ===
nomer = int(input())
print((nomer - 1) // 4 + 1)

# === Задача 7 ===
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
print("Сумма цифр =", a + b + c)
print("Произведение цифр =", a * b * c)

# === Задача 8 ===
num = int(input())
a = num % 10
b = (num // 10) % 10
c = num // 100
a, c = c, a
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")

# === Задача 9 ===
num = int(input())
print("Цифра в позиции тысяч равна", num // 1000)
print("Цифра в позиции сотен равна", (num // 100) % 10)
print("Цифра в позиции десятков равна", (num // 10) % 10)
print("Цифра в позиции единиц равна", num % 10)
