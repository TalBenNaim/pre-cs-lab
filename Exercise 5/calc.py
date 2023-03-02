more = True

while more == True:
    x = int(input("input a number: "))
    y = int(input("input a number: "))
    
    action = input("which action you want to take: / * + -")
    
    if action == '/':
        result = x / y
        
    if action == '*':
        result = x  * y
        
    if action == '+':
        result = x + y
        
    if action == '-':
        result = x - y
    
    print(result)
    answer = input("do you want to continue? press Y/N")
    
    if answer == "Y":
        more = True
    else:
        more = False    
    

    
    