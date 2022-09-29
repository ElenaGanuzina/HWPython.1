# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int (input("Enter figure "))
if 0 < a < 6:
    print ("It's workday!")
elif 5 < a < 8:
    print ("It's weekend!")
else:
    print("Oops! There's no such day of the week!")     