#!/usr/bin/python2.7

import random
import os


os.system('clear')
pieces=list("0123456789".upper())

def banner(sze):
        print("Place any of the following characters into their proper order.")
        print("You have "+str(sze)+" turns to guess the order")
        print("Available characters are: "+' '.join(pieces))
        print("Type 'quit' to exit.")
        print("\n\n")
        return True

def errorCheck(guess_str):
        guest_lst = list(guess_str)
        fail=[i for i in guest_lst if i not in pieces]
        if fail:
                 print(" ".join(fail)+" not selectable options")
                 return False
        if len(guest_lst) != size:
                print("Incorrect number of pieces chosen.  Place "+str(size)+" on board.")
                return False
        return True

def refreshScreen(lst):
        os.system('clear')
        banner()
        for turn in range(1,len(lst)):
                print("\t"+"| "+" ".join(lst[turn][0])+" | <=> |"+" ".join(lst[turn][1])+" |"+" Turn: "+str(lst[turn][2]))
        print("\n")
        return 1


size=input("How many pieces [3-6]?")
board=random.sample(pieces,size)
turns=[]
turns.append(board)
count=1
banner()

while (size*3) > count:
        #print(" "*size*2+"Turn: "+str(count))
        guess=raw_input("(Turn:"+str(count)+" of "+str(size*3)+"):")
        guess=guess.upper()
        if guess == "QUIT":exit(1)
        if not errorCheck(guess):
                continue
        hint=[]
        for b,g in zip(board,list(guess)):
                if b == g :
                        hint.append("C")
                        continue
                elif g in board:
                        hint.append("c")
                        continue
                else:
                        hint.append("X")
                        continue
        check=[i for i in hint if i == "C"]
        turns.append([list(guess),random.sample(hint,len(hint)),count])
        if len(check) == len(hint):
                print("You win!")
                exit()
        refreshScreen(turns)
        #rint("\t\t\t"+" ".join(random.sample(hint,len(hint)))+"->"+guess)
        count+=1
print("You lose!")
print("Correct sequence: "+" ".join(board))
exit(0)
