# FirstPhase / Day 3
# Задачи из главы 4_3

# === Задача 1 ===
n = int(input())
k = int(input())
if n < k:
    print("YES")
elif n > k:
    print("NO")
else:
    print("Don't know")

# === Задача 2 ===
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Равносторонний")
elif a != b and a != c and b != c:
    print("Разносторонний")
else:
    print("Равнобедренный")

# === Задача 3 ===
a = int(input())
b = int(input())
c = int(input())
mid = a
if mid < b < c or c < b < mid:
    mid = b
elif mid < c < b or b < c < mid:
    mid = c
print(mid)

# === Задача 4 ===
mon = int(input())
if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
    print(31)
elif mon == 2:
    print(28)
else:
    print(30)

# === Задача 5 ===
ves = int(input())
if ves < 60:
    print("Легкий вес")
elif ves < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

# === Задача 5 ===
a = int(input())
b = int(input())
do = input()
if do == "+":
    print(a + b)
elif do == "-":
    print(a - b)
elif do == "*":
    print(a * b)
elif do == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")

# === Задача 6 ===
a = input()
b = input()
if (a == "красный" or a == "синий" or a == "желтый") and (
    b == "красный" or b == "синий" or b == "желтый"
):
    if a == "красный" and b == "синий" or a == "синий" and b == "красный":
        print("фиолетовый")
    elif a == "красный" and b == "желтый" or a == "желтый" and b == "красный":
        print("оранжевый")
    elif a == "желтый" and b == "синий" or a == "синий" and b == "желтый":
        print("зеленый")
    else:
        print(a)
else:
    print("ошибка цвета")

# === Задача 6 ===
num = int(input())
if num == 0:
    print("зеленый")
elif (
    (1 <= num <= 10 or 19 <= num <= 28)
    and num % 2 == 1
    or (11 <= num <= 19 or 29 <= num <= 36)
    and num % 2 == 0
):
    print("красный")
elif (
    (1 <= num <= 10 or 19 <= num <= 28)
    and num % 2 == 0
    or (11 <= num <= 19 or 29 <= num <= 36)
    and num % 2 == 1
):
    print("черный")
else:
    print("ошибка ввода")

# === Задача 7 ===
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if b1 <= a1 <= b2 or b2 <= a1 <= b1:
    if b1 <= a2 <= b2 or b2 <= a2 <= b1:
        print(a1, a2)
    else:
        if a2 < b1 < b2 and b1 != a1:
            print(b1, a1)
        elif b2 < b1 < a2 and b1 != a1:
            print(a1, b1)
        elif a2 < b2 < b1 and b2 != a1:
            print(b2, a1)
        elif b1 < b2 < a2 and b2 != a1:
            print(a1, b2)
        else:
            print(a1)
elif b1 <= a2 <= b2 or b2 <= a2 <= b1:
    if a1 < b1 < b2 and b1 != a2:
        print(b1, a2)
    elif b2 < b1 < a1 and b1 != a2:
        print(a2, b1)
    elif a1 < b2 < b1 and b2 != a2:
        print(b2, a2)
    elif b1 < b2 < a1 and b2 != a2:
        print(a2, b2)
    else:
        print(a2)
elif a1 <= b1 <= a2 or a2 <= b1 <= a1:
    if a1 <= b2 <= a2 or a2 <= b2 <= a1:
        print(b1, b2)
    else:
        if b2 < a1 < a2 and a1 != b1:
            print(a1, b1)
        elif a2 < a1 < b2 and a1 != b1:
            print(b1, a1)
        elif b2 < a2 < a1 and a2 != b1:
            print(a2, b1)
        elif a1 < a2 < b2 and a2 != b1:
            print(b1, a2)
        else:
            print(b1)
elif a1 <= b2 <= a2 or a2 <= b2 <= a1:
    if b1 < a1 < a2 and a1 != b2:
        print(a1, b2)
    elif a2 < a1 < b1 and a1 != b2:
        print(b2, a1)
    elif b1 < a2 < a1 and a2 != b2:
        print(a2, b2)
    elif a1 < a2 < b1 and a2 != b2:
        print(b2, a2)
    else:
        print(b2)
else:
    print("пустое множество")
