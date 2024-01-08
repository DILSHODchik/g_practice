import random
guess = int(input("enter number between 1 and 5 : "))
ran = random.randint(1,5)
while(true):
     guess = int(input("enter number between 1 and 5 : "))
     if(guess == ran):
             print("CORRECT!")
             break
     else: print("WRONG! try again)
