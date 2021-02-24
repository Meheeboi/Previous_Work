#On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
#
#Pocket 0 is green.
#For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
#For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
#For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
#For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.

#Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black. 
#The program should display an error message if the user enters a number that is outside the range 0 through 36.


pocketNumber = int(input("Enter a pocket number to see whether green, red, or black."))

if pocketNumber == 0:
    print("0 is green.")
if (pocketNumber % 2 == 0) and (pocketNumber <= 10):
    print((pocketNumber), "is black.")
if (pocketNumber % 2 != 0) and (pocketNumber <= 10):
    print((pocketNumber), "is red")
if (pocketNumber % 2 == 0) and (11 < pocketNumber <= 18):
    print((pocketNumber), "is red.")
if (pocketNumber % 2 != 0) and (11 < pocketNumber <= 18):
    print((pocketNumber), "is black.")
if (pocketNumber % 2 == 0) and (19 < pocketNumber <= 28):
    print((pocketNumber), "is black.")
if (pocketNumber % 2 != 0) and (19 < pocketNumber <= 28):
    print((pocketNumber), "is red.")
if (pocketNumber % 2 != 0) and (29 < pocketNumber <= 36):
    print((pocketNumber), "is black.")
if (pocketNumber % 2 == 0) and (29 < pocketNumber <= 36):
    print((pocketNumber), "is red.")
if (pocketNumber > 36):
    print("That number is outside of the range 0-36.")

    