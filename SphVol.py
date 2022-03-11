import numpy as np

diametre = 0
radius   = 0

def calc(radius, diametre):
    if str(diametre) != "":
        radius = diametre/2
        vol = (4/3)*np.pi*(radius**3)

    else:
        vol = (4/3)*np.pi*(radius**3)
    
    print(vol)


def main(radius, diametre):
    x = True
    while x:
        test = input("Do you have a given radius or diametre: \n")
        if test == "y" or "n":
            x = False
        else:
            print("Please answer the question properly")


    if test == "y":
        diametre = int(input("What is your diametre: \n"))
    if test == "n":
        radius = int(input("What is your radius: \n"))


    calc(radius, diametre)


main(radius, diametre)