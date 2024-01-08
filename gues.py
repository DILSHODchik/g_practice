import random
guess = int(input("enter number between 1 and 5 : "))
ran = random.randint(1,5)
while(true):
     guess = int(input("enter number between 1 and 5 : "))
     if(guess == ran):
             print("you find it!")
             break
<<<<<<< HEAD
     else: print("NOPE! try again")
=======
     else: print("WRONG! try again")
>>>>>>> 6491720f421625de683f1ef90c2c41aac71bd34d
