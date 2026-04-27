# 1. Add Two Numbers
print("---- Add Two Numbers ----")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum =", sum)


# 2. Check Even or Odd
print("\n---- Even or Odd ----")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find Largest of Two Numbers
print("\n---- Largest Number ----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("a is largest")
else:
    print("b is largest")


# 4. Print 1 to 5 using Loop
print("\n---- Numbers from 1 to 5 ----")
for i in range(1, 6):
    print(i)


# 5. Factorial of a Number
print("\n---- Factorial ----")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial =", fact)