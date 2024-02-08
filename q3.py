#Write a program that takes an integer as input and returns true if the input is a power of two

def power_of_two(num):
    
    if num <= 0:
        return False
    
    return bin(num).count('1') == 1

input_num = int(input("Enter an integer: "))
result = power_of_two(input_num)
print(result)
