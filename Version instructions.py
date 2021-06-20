def instructions():
    inst=input("Do you need instructions to play? : answer 'y' for Yes and 'n' for No")
    if inst=="y":
        print("=======================================================================================")
        print("You will be given a set of four or three answers and you must choose which one is right")
        print("=======================================================================================")
    else:
        print("Welcome to the quiz")
        
instructions()#calling instructions function
