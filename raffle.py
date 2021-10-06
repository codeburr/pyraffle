from sys import exit
import os
import random

def clear():
    os.system("cls" if os.name=="nt" else "clear")
    return
def raffle(wins,shuffles=3):
    names=[]
    winners=[]
    with open("./names.txt","r") as f:
        lines=f.readlines()
        if wins<0: wins=abs(wins)
        if wins>len(lines): wins=len(lines)
        names=[line.rstrip() for line in lines]
        for i in range(0,wins):
            for j in range(0,shuffles):
                win=names[random.randint(0,len(names)-1)]
            winners.append(win)
            names.remove(win)
            print(str(i+1)+"- "+win)
    with open("./log.txt","w") as f:
        output=""
        for i in range(0,wins): 
            output+=winners[i]+(", " if i<wins-1 else "")
        f.write("Winners: "+output)
    return

clear()
proceed=False

with open("./names.txt","r") as f:
    if len(f.readlines())==0:
        print("'names.txt' is empty or inexistent.")
        input()
        exit(0)
print("How many winners?")
x=str(input()).strip()
while(not proceed):
    if not x.isnumeric():
        clear()
        print("Invalid. Please, input a valid integer.")
        x=str(input()).strip()
    else:
        if x=="0":
            clear()
            print("There's no need to raffle if there's no winners.")
            input()
            exit(0)
        else: proceed=True

clear()
proceed=False
print("How many shuffles? (Optional. Keep it empty to ignore.)")
y=str(input()).strip()
while(not proceed):
    if not y.isnumeric() and y!="":
        clear()
        print("Invalid. Please, input a valid integer or keep it empty.")
        y=str(input()).strip()
    else: 
        if y=="": y=3
        proceed=True

clear()
raffle(int(x),int(y))
