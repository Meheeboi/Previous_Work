

response =(input("Are you having computer problems?"))
if response == ("yes") or response == ("Yes"):
    print("Reboot the computer and try to connect.") 
    response2 = input("Did that fix the problem?")
    if response2 == "yes" or response2 == "Yes":
        print("Cool!")
        if response2 != "yes" or response2 != "Yes":
            print("Reboot the router and try to connect.") 
            response3 = input("Did that fix the problem?")
            if response3 == "yes" or response3 == "Yes":
                print("Cool!")
                if response3 != "yes" or response3 != "Yes":
                    print("Make sure the cables between the router and modem are plugged in firmly.") 
                    response4 = input("Did that fix the problem?")
                    if response4 == "yes" or response4 == "Yes":
                        print("Cool!")
                        if response4 != "yes" or response!= "Yes":
                            print("Move the router to a new location.") 
                            response5 = input("Did that fix the problem?")
                            if response5 == "yes" or response5 =="Yes":
                                print("Cool!")
                                if response5 != "yes" or response5 != "Yes":
                                    print("Get a new router.")

if response != "yes" or response != "Yes":
    print("Cool!")