# Problem 3 - Number Triangles
# Write a program that uses nested loops to display the triangular pattern
#  below. Note that the number of rows in the pattern should be specified 
# by the user at run time

num = int(input("Enter number of rows between 2 and 9"))
print("Number of rows:", num)
for x in range(0, num):
  for y in range(0,num-x):
    print(end=" ")
  for y in range (0,x+1):
    print(x+1, end=" ")
  if num < 2 or num > 9:
    raise ValueError("Number must be between 2 and 9")

  
  
  print()
