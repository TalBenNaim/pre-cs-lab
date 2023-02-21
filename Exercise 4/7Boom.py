limit = int(input("Insert a limit for the game: \n"))
numbers = range(1, limit + 1)

for num in numbers:
    if(num % 7 == 0 ) or ('7' in str(num)):
        print(f"{num} BOOM")
    else:
        print(num)