def main():
    try:
        total = int(input("Enter total cost of items"))
        num_items = int(input("Number of items"))
        average = total / num_items
    except ZeroDivisionError:
        print("Error: cannot have 0 items")
    except ValueError:
        print("Error: number of items cannot be negative")
main()

