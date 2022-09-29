# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

x1 = int(input("Enter x1 "))
y1 = int(input("Enter y1 "))
x2 = int(input("Enter x2 "))
y2 = int(input("Enter y2 "))

distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4) 
print(distance)