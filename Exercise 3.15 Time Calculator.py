#Exercise 3.15 - Time Calculator

#Write a program that asks the user to enter a number of seconds and works as follows:

#There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, 
#the program should convert the number of seconds to minutes and seconds.
#There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3600, 
#the program should convert the number of seconds to hours, minutes, and seconds.
 #There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, 
 #the program should convert the number of seconds to days, hours, minutes, and seconds.

time = int(input("Enter a number of seconds"))

days = int(time / 86400)
hours = int(((time % 86400) / 3600))
minutes = int((((time % 86400) % 3600) / 60))
seconds= (((time % 86400) % 3600) % 60)

print((days),"days,", (hours), "hours,", (minutes), "minutes,", (seconds), "seconds.")
