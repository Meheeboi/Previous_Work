def main():
    number = int(input("Enter a nonnegative integer: "))

    fact = factorial(number)

    print("The factorial of", number, "is", fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

main()


#---------------------------------------------------------
#GCD

def main():
    num1= int(input("Enter an integer"))
    num2 = int(input("Enter another integer"))

    print("The greatest common divisor of ")
    print("the two numbers is", gcd(num1, num2))

def gcd(x, y):
    if x % y == 0:
        return y
    else: 
        return gcd(x, x % y)

main()

#-------------------------------- FIB


def main():
    print("The first 10 numbers in the")
    print('Fibonacci series are: ')

    for number in range(1,11):
        print(fib(number))


def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else: return fib(n-1) + fib(n-2)

main()


#---------------------------- Recursion numbers in llist

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    my_sum = range_sum(numbers, 2, 5)

    print('The sum of items 2 through 5 is: ', my_sum)


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

main()

# Tower of Hanoi recursion problem

def main():
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg = 2


    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print("all the pegs are moved!")

def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print("Move a disc from peg", from_peg, "to peg", to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

main()
