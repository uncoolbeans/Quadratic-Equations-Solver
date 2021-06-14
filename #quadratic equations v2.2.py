#quadratic equations v2.2


from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
import math



def discriminant(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant > 0:
        print("Equation has 2 real and distinct roots.")
    elif discriminant == 0:
        print("Equation has 2 real and equal roots.")
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

def coordinatesFind(min,max,a,b,c,increment):
    print("\nBelow are coordinates for the graph.(Note: values are rounded to 2 d.p. where applicable.)")
    x = min
    xCordList = []
    yCordList =[]
    cordsTable = PrettyTable(["x","y"])
    while x <= max:
        y = (a*(x**2))+(b*x)+c
        x = round(x, 2)
        y = round(y,2)
        xCordList.append(x)
        yCordList.append(y)
        cordsTable.add_row([str(x),str(y)])
        x+=increment
    print(cordsTable)
    plt.plot(xCordList,yCordList)
    plt.show()

def restart():
    while True: 
        restart = input("Restart? (y/n): ")
        if restart == "y":
            print("Restarting...\n")
            return True
            break
        elif restart == "n":
            print("Terminating...\n")
            return False
            break
        else:
            print("Invalid input. Re-enter.")

def quadraticFormula(a,b,c):
    discriminant = (b**2)-(4*a*c)
    if discriminant == 0:
        sol = (- b + math.sqrt(discriminant))/(2*a)
        print(f"The root of the equation is {sol} (rounded to 2 d.p.).\n")
    elif discriminant > 0:
        sol1 = (- b + math.sqrt(discriminant))/(2*a)
        sol2 = (- b - math.sqrt(discriminant))/(2*a)
        print(f"The roots of the equation are {round(sol1,2)} and {round(sol2,2)} (rounded to 2 d.p.).\n")


def main():
    start = True
    while start:
        print("Welcome to the quadratic equatvaion solver! Please enter your values in the following sequence ax^2+bx+c=0.\nThe program will automatically solve for x and find the coordinates of points for the graph of the equation, as well as weather it has real roots.")
        valuesList = convert_Input_To_Int()
        discriminant(valuesList[0],valuesList[1],valuesList[2])
        quadraticFormula(valuesList[0],valuesList[1],valuesList[2])
        print("Please enter maximum and minimum x range for coordinates finder.")
        max_min_list = maxMinRecieve()
        while True:
            increment = input("X-value increments (floats and integers accepted, do not enter 0): ")
            try:
                increment = float(increment)
                break
            except ValueError:
                print("Invalid input. Try again.\n")
        coordinatesFind(max_min_list[1],max_min_list[0],valuesList[0],valuesList[1],valuesList[2],increment)

        start = restart()

        



main()