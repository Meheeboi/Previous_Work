
totalRain = 0
userYears = int(input("Number of years to calculate rainfall"))


for year in range(1, userYears +1):
    for month in range(1,13):
        monthRain = float(input("rainfall this month"))
        totalRain += monthRain
        monthTotal = userYears * 12

avgRain = totalRain / monthTotal

print("Average Rain Per Month = ", avgRain, "inches",\
    "Total Months = ", monthTotal, "months", \
        "Total Rain = ", totalRain, "inches")