#Write a program that counts the number of vowels in a sentence

def count_vowels(sentence):
    
    vowels = set("aeiouAEIOU")

    vowel_count = sum(1 for char in sentence if char in vowels)

    return vowel_count

input = input("Enter a sentence: ")

result = count_vowels(input)

print("Number of vowels:", result)



