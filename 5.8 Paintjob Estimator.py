# A painting company has determined that for every 112 square feet of wall 
# space, one gallon of paint and eight hours of labor will be required. 
# The company charges $35.00 per hour for labor. 
# Write a program that asks the user to enter the square feet of wall space 
# to be painted and the price of the paint per gallon. 

# The program should display the following data:

# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job

import math

get_footage = float(input("Square Footage of walls to paint?"))
get_paint = float(input("Cost of paint per gallon?"))


v = get_footage / 112
w = (get_footage / 112) * 8
x = (get_paint)
y = (((get_footage / 112) * 8) *35)
z = (get_paint) + (((get_footage / 112) * 8) *35)


print("You require: ", v, "Gallons of Paint\n", 
    w, "hours of labor\n",
    "$", x, "for paint costs\n",
    "$", y, "for labor costs\n",
    "Total Job Costs are : $", z)
  




    
