print('Hi! Welcome to the Roll optimizer!')
print('ATF = Add To Face Value')

inputAmount = 4

currentShop = []

def Inputs():
    userInput = str(input("What kind of upgrade?")).upper()
    if userInput == "ATF":
        ATFInput()
    else:
        Inputs()

def ATFInput():
    currentShop.append(["ATF", int(input("What is the number that is going to be added to the face?")), int(input("What is the cost of the upgrade?"))])

for i in range(inputAmount):
    Inputs()

print(currentShop)