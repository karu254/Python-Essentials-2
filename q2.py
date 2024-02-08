#Write a program to generate the Fibonacci sequence up to 100.

x, y = 0, 1

while x <= 100:
    print(x, end=", ")
    x, y = y, x + y
