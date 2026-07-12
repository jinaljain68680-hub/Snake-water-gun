import random
computer=random.choice([1,0,-1])

youdict={"s":1,"w":0,"g":-1}
reversedict={1:"s",0:"w",-1:"g"}
youstr = input("Enter s, w or g: ")
you = youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")
if(computer==you):
    print("its draw")
else:
    if(computer==1 and you==0):
        print("win")
    elif(computer==1 and you==-1):
        print("win")
    elif(computer==0 and you==1):
        print("win")
    elif(computer==0 and you==-1):
        print("lose")
    elif(computer==-1 and you==0):
        print("lose") 
    elif(computer==-1 and you==1):
        print("win")
    else:
        print("something went wrong")   