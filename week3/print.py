"""week-3 task: Write a program that prints numbers from 0 to 99.
- Numbers must be separated by ,, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module
"""
def format_number(n):
    if n < 10:
     return f"0{n},"
    else:
     return f"{n},"
print("00, ", end="")
for i in range(1, 100):
        num = format_number(i)
        if i != 99:
            print(num, end=" ")
        else:
            print(num)
