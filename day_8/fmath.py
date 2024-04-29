import math
print("One can can paint 5 square meters")
height=float(input("heigt of the wall is: "))
width=float(input("width of the wall is: "))
per_can=float(input("Coverage per can"))

def color_need(height,width,per_can):
    print(f'color need is{height} * {width} / {per_can}= {math.ceil((height*width)/per_can)}')

color_need(width,height,per_can)
