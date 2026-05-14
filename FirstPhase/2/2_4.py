# FirstPhase / Day 2
# Задачи из главы 2.4

# === Задача 1 ===
num = int(input())
print(num)
print(num + 1)
print(num + 2)

# === Задача 2 ===
print(int(input()) + int(input()) + int(input()))

# === Задача 3 ===
print((int(input()) + int(input()) + int(input()) + int(input())) * 3)

# === Задача 4 ===
a = int(input())
b = int(input())
print(3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41)

# === Задача 5 ===
num = input()
print("Следующее за числом", num, "число:", int(num) + 1)
print("Для числа", num, "предыдущее число:", int(num) - 1)

# === Задача 6 ===
a = int(input())
v = a * a * a
s = 6 * a * a
print("Объем =", v)
print("Площадь полной поверхности =", s)

# === Задача 7 ===
a = int(input())
b = int(input())
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

# === Задача 8 ===
a = int(input())
d = int(input())
n = int(input())
print((n - 1) * d + a)

# === Задача 9 ===
x = int(input())
print(x * 1, x * 2, x * 3, x * 4, x * 5, sep="---")
