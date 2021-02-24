

#Write a Python program that defines and calls the functions below to do 
# the following:

#1) getNumbers(): generate and return 5 random numbers between 1 and 10.

#2) getLowest(): receive as parameters the 5 random number returned by 
# the getNumbers() function and returns the lowest number.

#3) getHighest(): receive as parameters the 5 random number returned 
# by the getNumbers() function and returns the highest number.

#4) getModifiedAverage(): receive as parameters the 5 random number 
# returned by the getNumbers() function, the lowest value returned by 
# the getLowest() function, and the highest value returned by the 
# getHighest() function and return the average of the five numbers 
# after dropping the highest and lowest values.

import random
from statistics import mean


randList = []
for i in range(0,5):
    randList.append(random.randint(0,10))
    avg = mean(randList)
    


print("The five generated random numbers are:", randList, '\n'"The average of the numbers is:",avg, '\n' "The lowest number is:", min(randList),
'\n' "The highest number is:", max(randList))

randList.remove(min(randList))
randList.remove(max(randList))
avg = mean(randList)

print("The average after dropping the lowest and highest numbers is:", "{:.2f}".format(avg))