"""week-3 task2:Write a program that prints the following pattern.
The program should accept the input for character
The pattern consists of a series of lines
The characters in each line should follow a specific pattern based on the line number.
Use conditional statements to determine the pattern for each line.
Use a loop to iterate through the lines and print the characters accordingly.
You are not allowed to use functions in your code.
Do not store the pattern or any intermediate results in variables.
"""
character = input("please enter the pattern to be printed: ")
if len(character)>1:
    print("The length of the character should be one")
    character = input("please enter the pattern to be printed: ")
if character in "aeiou":
    print("vowels not allowed in the input")
    character = input("please enter the pattern to be printed: ")
for line in range(1,6):
    if line == 1:
        print(character)
    else:
        print(character * line)
