import random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]

print(f"You choose: {reverseDict[you]}\n Computer Choose: {reverseDict[computer]}")
if computer==you:
    print("It is draw")
else:
    if((computer-you==-1 or computer-you==2 )):
        print("You lose")
    else:
        print("You win")