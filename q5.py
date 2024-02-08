#Write a program that takes an integer as input and returns an integer with reversed digit 
#ordering

def reverse_integer(input_integer):

    reversed_string = str(input_integer)[::-1]


    if input_integer < 0:
   
        reversed_string = reversed_string[:-1]

        reversed_integer = int(reversed_string) * -1
    else:
    
        reversed_integer = int(reversed_string)

    return reversed_integer


user_input = int(input("Enter an integer: "))


result = reverse_integer(user_input)

print("Reversed integer:", result)



