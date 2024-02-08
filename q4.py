#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string

def capitalize_string(input_string):
    
    string_result = input_string.title()
    return string_result

user_input = input("Enter a string: ")

result = capitalize_string(user_input)

print("Result:", result)


