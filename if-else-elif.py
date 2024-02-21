# firstname="guvi13"
# lastname="guvi"
# if(firstname==lastname):
#     print("Yes")
# else:
#     print("Else")

# print("No")

age=int(input("Enter the age:\n"))
if(age<18):
    print("You cannot Vote")

elif(age==18):
    print("You can vote if you have voter ID")

    if(True):
        print("Yes")
    
    if(age<15):
        print("No")
    else:
        print("OK")
        if(10=='10'):
            print('10')
        else:
            print('20')


elif(age>=18 and age<=70):
    print("You can vote")

else:
    print("Good Bye")