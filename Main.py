#import random for dice rolling
import random

#welcome statment
print("Hello! Welcome to Farm Game",)

#initialize start position and die roll
P_Position  = 1
RollNum = 0

#initialize game funds and resources
P_Cash      = 5000
P_Debt      = 5000

P_EquipmentTractor = 0
P_EquipmentCombine = 0

P_CropWheat = 10
P_CropHay   = 10
P_CropFruit = 5
P_Livestock = 10

#code to exit game
exitstate = "y"

#function to roll die
def Roll():
    return random.randint(1,6)
    
#funtion to specify if the user is able to but equipment
def buySeason():
    if (P_Position < 20):
        return 1
    else :
        return 0

#function to add role to the current postion and to restart the board   
def boardPosition(roll, currentSquare):
    result = roll + currentSquare
    if result > 50:
        result -= 50
    return result
    
#fuction to find if player has landed on a crop square
def cropHarvest(currentpos):
    if currentpos in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,50]:
        return 0
    elif currentpos in [21,22,23,24,27,28,29,35,36,41,42]:
        return 1
    elif currentpos in [30,31,32,33,34,47,48,49]:
        return 2
    elif currentpos in [24,25,26,43,44,45,46]:
        return 3
    elif currentpos in [37,38,39,40]:
        return 4
    else:
        return 0

def harvestCalc(roll,croptype):

    if croptype == 1:
        print("havest value:",(50*roll*P_CropHay))
        return (50*roll*P_CropHay)
    elif croptype == 2:
        print("havest value:",(100*roll*P_CropWheat))
        return (100*roll*P_CropWheat)
    elif croptype == 3:
        print("havest value:",(250*roll*P_CropFruit))
        return (250*roll*P_CropFruit)
    elif croptype == 4:
        print("havest value:",(120*roll*P_Livestock))
        return (120*roll*P_Livestock)
    else:
        print("no harvest")
        return (0)

    
#while function to house the game
while exitstate != "n":
    print("\n")
    print("     Week:",P_Position,"Cash :$",P_Cash,"Debt :-$",P_Debt,)
    print("     Tractor",P_EquipmentTractor,"Combine",P_EquipmentCombine)
    print("     Wheat",P_CropWheat,"Hay", P_CropHay, "Fruit", P_CropFruit,"Cattle", P_Livestock)
    exitstate = input("\n Contine? y-n ")
    RollNum = Roll()
    print("You've rolled ",RollNum)
    P_Position = boardPosition(P_Position, RollNum)
    print(cropHarvest(P_Position))
    print(buySeason())
    P_Cash = (P_Cash + harvestCalc(RollNum,cropHarvest(P_Position)))


    
    
