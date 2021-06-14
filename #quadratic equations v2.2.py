#quadratic equations v2.2


from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np


def discriminant(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant > 0:
        print("Equation has 2 real and distinct roots.\n")
    elif discriminant == 0:
        print("Equation has 2 real and equal roots.\n")
    elif discriminant < 0:
        print("Equation has no real roots.\n")


def convert_Input_To_Int():
    lst = ["a","b","c"]
    convertedLst =[]
    for x in lst:
        while True:
            convertedInt = input(f"Enter value of {x}: ")
            try:
                convertedInt = int(convertedInt)
                convertedLst.append(convertedInt)
                break
            except ValueError:
                print("Invalid input. Try again.\n")
    return convertedLst

def maxMinRecieve():
    lst =[]
    while True:
        while True:
            max = input("Enter maximum value:  ")
            try:
                max = int(max)
                break
            except ValueError:
                print("Invalid input. Try again.")
        while True:
            min = input("Enter minimum value:  ")
            try:
                min = int(min)
                break
            except ValueError:
                print("Invalid input. Try again.")
        if max <= min:
            print("Error, maximum value is smaller than or equal to minimum, please check again.\n")
        else: 
            lst.append(max)
            lst.append(min)
            break
    return lst

def coordinatesFind(min,max,a,b,c):
    print("\nBelow are coordinates for the graph.")
    
    x = min
    xCordList = []
    yCordList =[]
    cordsTable = PrettyTable(["x","y"])
    while x <= max:
        y = (a*x**2)+(b*x)+c
        xCordList.append(x)
        yCordList.append(y)
        cordsTable.add_row([str(x),str(y)])
        x+=1
    print(cordsTable)





def main():
    print("Welcome to the quadratic equatvaion solver! Please enter your values in the following sequence ax^2+bx+c=0.\nThe program will automatically solve for x and find the coordinates of points for the graph of the equation, as well as weather it has real roots.")
    valuesList = convert_Input_To_Int()
    discriminant(valuesList[0],valuesList[1],valuesList[2])
    print("Please enter maximum and minimum x range for coordinates finder.")
    max_min_list = maxMinRecieve()
    coordinatesFind(max_min_list[1],max_min_list[0],valuesList[0],valuesList[1],valuesList[2])


        



main()