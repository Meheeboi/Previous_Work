for x in range(2,101):
    prime = True
    for i in range(2,x):
        if (x % i == 0):
            prime = False
    if prime:
       print (x)