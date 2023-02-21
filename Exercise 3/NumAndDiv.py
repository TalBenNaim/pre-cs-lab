num = float(input("Insert a number: \n"))
div = float(input("Insert a div: \n"))

if div == 0:
    print("Div can't be 0.")
elif num % div == 0:
    print("This number is a multiple of div.")
else:
    print("This number is not a multiple of div.")

# for readbility reasons putting else instead of elif would be better here

# different option
# if div != 0: first and reverse the order

#also can get a exit() or somth to exit in the if and discard the else
