import matplotlib.pyplot as plt
import numpy as np
import math

def best_fit(xpoints, ypoints):

    xbar = sum(xpoints)/len(xpoints)
    ybar = sum(ypoints)/len(ypoints)
    n = len(xpoints) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(xpoints, ypoints)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in xpoints]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b


# y-coordinates are set (selected Back-End register), x-coordinates keep changing (many different Front-End registers)
ycoord = [0,2,6,9,13]
angleList =[]

while (True):

    xcoord = []
    # if the x coordinate for the first point is negative, stop drawing because no more graphs (no data would have a negative failure rate)
    x1 = input("Enter a x coordinate for the first point: ")
    x1 = float(x1)
    if (x1 < 0):
        break
    xcoord.append(x1)
    for i in range(len(ycoord)-1):
        x2 = input("Enter a x coordinate for the point: ")
        x2 = float(x2)
        xcoord.append(x2)


    #print("The points are:")

    for i in range(len(xcoord)):
        print("(" + str(xcoord[i]) + "," + str(float(ycoord[i])) + ")!")


    a,b = best_fit(xcoord,ycoord)


# Plot Graph
    angle = math.degrees(np.arctan(b))
    angleList.append(angle)
    print("The angle of the slope is " + str(angle) + " degrees!\n")

    plt.scatter(xcoord, ycoord)
    yfit = [a + b * xi for xi in xcoord]
    plt.xlabel('Front End Fail Rate')
    plt.ylabel('Back End Fail Rate')
    plt.plot(xcoord, yfit)
    plt.draw()

print("The respective angles of the slopes are: ")
print(angleList)

#Compare the angles to see which line is closest to 45 degrees
smallestDifference = abs(angleList[0] - 45.0)
index = 0
for i in range(1,len(angleList)):
    currentDifference = abs(angleList[i] - 45.0)

    if(currentDifference < smallestDifference):
        smallestDifference = currentDifference
        index = i

if (index+1 is 1):
    print("The best fit line is the {}st line and the angle is {}".format(index+1,angleList[index]))
elif (index+1 is 2):
    print("The best fit line is the {}nd line and the angle is {}".format(index+1,angleList[index]))
elif (index+1 is 3):
    print("The best fit line is the {}rd line and the angle is {}".format(index+1,angleList[index]))
else:
    print("The best fit line is the {}th line and the angle is {}".format(index+1,angleList[index]))

plt.show()



# point2 = []
# x2,y2 = input("Enter a pair of x-y coordinates for the 2nd point: ").split()
# x2 = float(x2)
# y2 = float(y2)
# point2 = [x2,y2]



# print("The 1st coordinate is (" + str(x1) + "," + str(y1) + ")." )
# print("point1 is (" + str(point1[0]) + "," + str(point1[1]) + ").")
# print("The 2nd coordinate is (" + str(x2) + "," + str(y2) + ")." )
# print("point2 is (" + str(point2[0]) + "," + str(point2[1]) + ").")

# slope1 = (y2-y1) / (x2-x1)
# print("The slope of this line is " + str(slope1) + " !") 

