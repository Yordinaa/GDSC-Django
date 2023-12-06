"""week-3 task3: Develop a program that checks if a user-inputted word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., "radar")."""
print("Please enter a word to check: ")
word = input().lower()
# for case-insensitive palindrome checking
reverse = word[::-1]
if word == reverse:
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome")
