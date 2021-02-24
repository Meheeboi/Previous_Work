# Modify the program that you wrote for Exercise 6 so 
# it handles the following exceptions:

# It should handle any IOError exceptions that are raised when the file 
# is opened and data is read from it.

# It should handle any ValueError exceptions that are raised 
# when the items that are read from the file are converted to a number.  

def main():
    try
        myfile = open("numbers.txt", 'r')

        total = 0
        numLines = 0
        lineCount = myfile.readline()

        while lineCount != "":
            numLines += 1
            total += int(lineCount)
            lineCount = myfile.readline()


        average = total / numLines

        myfile.close()

        print( "Average of numbers in file is:", average)
    
    except (IOError, ValueError):
        print("File does not exist/ Input or Output invalid/ Value is invalid.")


main ()


