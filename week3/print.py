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
