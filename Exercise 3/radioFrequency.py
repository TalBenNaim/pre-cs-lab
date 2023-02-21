radioFrequency = int(input("Which radio frequency you want to broadcast on? \n"))

if radioFrequency >= 88 and radioFrequency <= 107:
    print("Great! enjoy broadcasting.")
else:
    print("The radio frequency you entered is unavailable.")