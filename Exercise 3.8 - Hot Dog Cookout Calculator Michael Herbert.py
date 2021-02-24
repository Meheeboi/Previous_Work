numPeople = int(input("How many people are coming?"))
desiredDogs= int(input("How many dogs per person?"))


totalDogs = numPeople * desiredDogs
dogPack = totalDogs / 10
bunPack = totalDogs / 8


if (totalDogs % 10) == 0 and (totalDogs % 8) == 0:
    print ("You will need a minimum of", (dogPack), "hot dog packs and", (bunPack), "hot dog bun packs, and will have zero leftover hot dogs or buns")
if totalDogs <= 10:
    print("You will need a minimum of one pack of hot dogs and two packs of hot dog buns with 0 hot dugs and 6 buns left over")
if (totalDogs % 10) > 0 and (totalDogs % 8) > 0:
    print("You will need a minimum of", (int(dogPack)+1), "hot dog packs and", ((totalDogs // 8) +1 ), "hot dog bun packs, but will have", 
    (10 - (totalDogs % 10)), "leftover hot dogs and", (8-(totalDogs % 8)), "leftover hot dog buns.")
if (totalDogs % 10) == 0 and (totalDogs % 8) > 0:
    print("You will need a minimum of", (int(dogPack)), "hot dog packs and", (int(bunPack) + 1), "hot dog bun packs with", (totalDogs % 10), 
    "leftover hot dogs and", (totalDogs % 8), "leftover hot dog buns.")
if (totalDogs % 8 ) == 0 and (totalDogs % 10) != 0:
    print ("You will need a minimum of", (int(bunPack)), "hot dog bun packs and", (int(dogPack) +1),"hot dog packs with 0 leftover buns and",
     (10 - (totalDogs % 10)), "leftover hot dogs.")
