# inspiration code for Python Unit Testing Project
import math

def surfaceArea(rad):
    #surface area: 4 * pi * r^2
    area = 4 * math.pi * rad * rad
    return area


#volume: (4/3) * pi * r^3
def volume(rad):
    volume = (4/3) * math.pi * rad * rad * rad
    return volume

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))

    print("\nThe Volume of a Sphere = ", volume(radius))
    print("\nThe Surface Area = ", surfaceArea(radius))

if __name__ == '__main__':
    prompt()
