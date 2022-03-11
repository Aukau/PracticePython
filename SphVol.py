import numpy as np

def calc(radius, diametre):
    if int(diametre) != 0:
        radius = diametre/2
        vol = (4/3)*np.pi*(radius**3)

    else:
        vol = (4/3)*np.pi*(radius**3)
    
    print(vol)


def main():
    x = True
    diametre = 0
    radius = 0
    while x:
        test = input("Do you have a given radius or diametre: \n")
        if test == "radius" or "diametre":
            x = False
        else:
            print("Please answer the question properly")


    if test == "diametre":
        diametre = int(input("What is your diametre: \n"))
    if test == "radius":
        radius = int(input("What is your radius: \n"))


    calc(radius, diametre)

main()
