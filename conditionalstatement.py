# python script that checks if a number is even or odd number

num=int(input("Enter a number: "))

if num %2==0:
    print(f"{num} is Even number")
else:
    print(f" {num} is Odd number")


   # create a program that prints the largest of three numbers

num2=int(input("Enter the first number: "))
num3=int(input("Enter the second number: "))
num4=int(input("Enter the third number: "))

if num2<num4:
    print(f"{num2} is smaller than {num4}")
if num3<num4:
    print(f"{num4} is larger than {num3}")
if num3>num2:
    print(f"{num3} is larger than {num2}")
if num2<num3:
    print(f"{num2} is smaller than {num3}")

