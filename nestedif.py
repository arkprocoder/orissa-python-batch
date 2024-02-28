a=10
b=20
if(a<b):
    print("i am if")
    if(True):
        print("i am first if of if")
    else:
        print("i am else of first if")

        if(True):
            print("True")

else:
    print(" i am else")
    if(False):
        print("i am else if of if")

    elif(False):
        print("i am el if")
    else:
        print("i am else of first else")

        if(True):
            print("True")    