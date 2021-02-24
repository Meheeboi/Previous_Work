#Employee earns 1 penny the first day, doubling each consecutive day of work. 
#Ask user for number of days to calculate.
#Display TABLE showing the earning for each day, with total at the end.
#Output should be in Dollars, not numbers of pennies


pay = 1 
totalPennies = 0
daysWorked = int(input("How many days will you work?"))

print ()

print( "Day #", "\t", "Salary (Number of Pennies)")
for days in range ( daysWorked ):
    realPay = (2 ** days) 
    totalPennies += realPay
    print ( days +1, "\t", realPay )

totalPay = totalPennies * .01
print ()
print ( "Total Pay = $", totalPay )


    



