def calc():
    userinput = input("Weclome to MyCalc, please choose a number \n")
    number = int(userinput)
    Mode = {1: "add", 2: "subtract", 3: "multiply", 4: "divide" }
    opteration = []
    choosemode = input("What would you like to do, 1 - add, 2 - subtract, 3 - multiply , 4 - divide\n ")
    choosemode = int(choosemode)
    if choosemode == 1 or choosemode == 2 or  choosemode == 3 or choosemode == 4 :
        print("You've chosen: ", Mode[choosemode])
        if choosemode == 1:
            userinput = input ("Chose another number: ")
            output =  number + int(userinput)
            
        elif choosemode == 2:
            userinput = input ("Chose another number: ")
            output =  number - int(userinput)
            
        elif choosemode == 3:
            userinput = input ("Chose another number: ")
            output =  number * int(userinput)
            
        elif choosemode == 4:
            userinput = input ("Chose another number: ")
            output =  number / int(userinput)
            
    else: 
        print("You didn't chose a valid options")
    return output
print(calc())