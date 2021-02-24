# At one college, the tuition for a full-time student is $8,000 per semester. 
# It has been announced that the tuition will increase by 3 percent 
# each year for the next 5 years. 
# Write a program with a loop that displays the projected semester tuition 
# amount for the next 5 years.



startingTuition = 16000
increasedTuitionRate = 3/100
resultTuition = 0

print ("From this year, tuition will increase by 3 percent each year. \nThe next five years will find your Tuition increased to:")

print()
print("Year", "\t", "Tuition")
for year in range (5):
    startingTuition += (( increasedTuitionRate) * startingTuition)
    resultTuition += startingTuition
    print(year +1, "\t", ("{:.2f}".format(startingTuition)))






