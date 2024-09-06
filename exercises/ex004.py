number = int(input("Say a number from 1 to 100: \n"))
while True:
    if number > 50 and number < 100:
            print("Correct")
            break
    elif number < 1 or number > 100:
        number = int(input("1 to 100\n"))
    else:
        number = int(input("Incorrect\n"))