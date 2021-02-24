def main():
    #get three names
    print("enter three numbers")
    name1 = input(" #1: ")
    name2 = input(" #2: ")
    name3 = input(" #3: ")


    #open file named friends.txt.
    myfile = open("numbers.txt", 'w')

    #write names to the file
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    #close the file
    myfile.close()
    print("The numbers that were written to numbers.txt = ", name1, name2, name3)

#call main function
main()

