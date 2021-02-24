oCookies = 48
oSugar = 2
oButter = 1.5
oFlour = 1



desiredCookies = int(input("How many cookies boy?"))

print ("For", desiredCookies, "cookies you need...")

desiredFlour = (desiredCookies/oCookies) * oFlour
desiredSugar = (desiredCookies/oCookies) * oSugar
desiredBdutter = (desiredCookies/oCookies) * oButter

print ((desiredBdutter), "cups of butter,", (desiredFlour), "cups of Flour, and", (desiredSugar), "cups of Sugar.")