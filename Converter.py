# Author Przemysław Pyk
# Maracui
# 25.09.2018


def milesToKilometersConverter():
    print("Write distance in miles: ")
    miles = float(input())
    distanceInKilometers = miles * 1.609344
    print("Your distance in kilometers is equal ",  distanceInKilometers)


def kilometersToMilesConverter():
    print("Write distance in kilometers: ")
    kilometers = float(input())
    distanceInMiles = kilometers * 0.621371192
    print("Your distance in miles is equal ", distanceInMiles)


def kilometersToFeetConverter():
    print("Write distance in kilometers: ")
    kilometers = float(input())
    distanceInFeet = kilometers * 3280.8399
    print("Your distance in feet is equal ", distanceInFeet)


def feetToKilometersConverter():
    print("Write distance in feet: ")
    feet = float(input())
    distanceInKilometers = feet * 0.0003048
    print("Your distance in kilometers is equal ", distanceInKilometers)


def natuicalMilesToKilometersConverter():
    print("Write distance in natuical miles: ")
    nauticalmiles = float(input())
    distanceInKilometers = nauticalmiles * 1.85200
    print("Your distance in kilometers is equal ", distanceInKilometers)


def kilometersToNauticalMilesConverter():
    print("Write distance in kilometers: ")
    kilometers = float(input())
    distanceInNauticalMiles = kilometers * 0.539956803
    print("Your distance in nautical miles is equal ", distanceInNauticalMiles)

print("Welcome in Python Distance Converter")
while True:
    print("\n1. Convert miles to kilometers")
    print("2. Convert kilometers to miles")
    print("3. Convert feet to kilometers")
    print("4. Convert kilometers to feet")
    print("5. Convert nautical miles to kilometers")
    print("6. Convert kilometers to nautical miles")
    print("7. Exit")
    userDecision = int(input())
    if userDecision == 1:
        milesToKilometersConverter()
    elif userDecision == 2:
        kilometersToMilesConverter()
    elif userDecision == 3:
        feetToKilometersConverter()
    elif userDecision == 4:
        kilometersToFeetConverter()
    elif userDecision == 5:
        natuicalMilesToKilometersConverter()
    elif userDecision == 6:
        kilometersToNauticalMilesConverter()
    elif userDecision == 7:
        exit()
    else:
        print("Wrong number has been written")
