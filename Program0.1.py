
# Square Shape print function is definied on startup to clear clutter #
def SquareShape():
    print("  X  ")
    print("-----")
    print("|   | Y")
    print("-----")

print("==============V0.1==========================\n\n\n\n=================Menu=======================\n")
MenuSelection = int(input("This is the Dunsch Area Perimeter Program (DAPP).\nThere are 3 modes in this program:\n\n1. Calculator\n2. Game\n3. Teacher\n\nPress the number of the mode you want to select.\nInput: "))

# Mode 1 #
if MenuSelection == 1:
    Mode1Shape = str.upper(input("============================================\n\nWelcome to the Calculator!\nHere, you can specify a shape and its side lengths for me to work out.\nwhich shape do you want? Square/Rectangle or a Triangle?\nInput: "))

    if (Mode1Shape == "SQUARE") or (Mode1Shape =="RECTANGLE"):
        SquareShape()
        Mode1X = int(input("In Centimeters, how long is X? "))
        Mode1Y = int(input("In Centimeters, how long is Y? "))
        Mode1SquareArea = Mode1X * Mode1Y
        Mode1SquareRim = Mode1X + Mode1Y
        print("Area:", Mode1SquareArea, "\nPerimeter:", Mode1SquareRim)
        
    elif (Mode1Shape == "TRIANGLE"):
        Mode1TriangleType = int(input("============================================\nWhich type of triangle?\n1 - Right Angled\n2 - Equilateral\n3 - Iscoseles\n4 - Scalene\nInput: "))
        if Mode1TriangleType == 1:
            print("============================================\nYou selected Right Angled.")
        elif Mode1TriangleType == 2:
            print("============================================\nYou selected Equilateral.")
        elif Mode1TriangleType == 3:
            print("============================================\nYou selected Equilateral")
        elif Mode1Triangletype == 4:
            print("============================================\nYou selected Scalene.")

# Mode 2 #
elif MenuSelection == 2:
    print("============================================\n\nWelcome to the Game!\nHere, you can play an area & perimeter calculation game with me. Can you beat the computer?")

# Mode 3 #
elif MenuSelection == 3:
    print("============================================\n\nWelcome to the Teacher!\nHere, I will teach you how to solve areas and perimeters of various shapes.")
    
  

