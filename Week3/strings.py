#!/usr/bin/env python3 

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Question 1
print("Hello",varName)

#Question 2
print(varRed,"-",varGreen,"-",varBlue)

#Question 3
print("Is this ",varGreen,"or",varBlue,"?")

#Question 4
print("My name is ",varName.upper())

#Question 5
print(f"{varRed:+^7s}")

#Question 6
print(f"{varGreen:=<7s}")

#Question 7
print(f"{varBlue:*>9s}")

#Question 8
print(varBlue*10)

#Question 9
print(varLoot)

#Question 10
print(f"{varLoot: <.1f}")

#Question 11
print("I have $",f"{varLoot: <.2f}")

#Question 12
print(f"{varRed:$^10s},{varGreen:$^10s},{varBlue:$^10s}")

#Question 13
print(varRed[::-1],varGreen,varBlue[::-1])

#Question 14
print("First Color:",varRed,"Second Color:",varGreen,"Third Color:",varBlue)
