import random
Ceil = input("Give us a upper limit")
random_number = random.randint( 1 , int(Ceil))
guess = 0
while guess != random_number :
     guess = int(input("guess the number"))

     if guess < random_number:
         print("My number is still a bit higher , Try again")

     elif guess > random_number:
         print ("My number is a bit low , Try again")

print("Congratulations, you won the game")

