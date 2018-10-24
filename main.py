import math
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculateRealSpiral(pitch, a, iterations, theta0, dTheta, dZ):
    pitch = pitch / 180 * math.pi
    phi = math.pi / 2 - pitch
    b = 1 / math.tan(phi)

    #print("pitch: {}, a: {}, b: {}".format(pitch, a, b))

    calculateR = lambda theta : a * math.exp(b * theta)

    theta = theta0
    r = calculateR(theta0)
    z = 0

    x_list = [r * math.cos(theta)]
    y_list = [r * math.sin(theta)]
    z_list = [z]

    for i in range(iterations):
        theta -= dTheta
        r = calculateR(theta)
        z -= dZ

        x_list.append(r * math.cos(theta))
        y_list.append(r * math.sin(theta))
        z_list.append(z)

    return [x_list, y_list, z_list]

def calculateFakeSpiral(pitch, a, iterations, theta0, dTheta, dZ):
    pitch = pitch / 180 * math.pi
    phi = math.pi / 2 - pitch
    b = 1 / math.tan(phi)

    theta = theta0
    r = a * math.exp(b * theta)
    z = 0

    x_list = [r * math.cos(theta)]
    y_list = [r * math.sin(theta)]
    z_list = [z]

    for i in range(iterations):
        theta -= dTheta
        r = (math.sin(phi) / math.sin(phi + dTheta)) * r
        z -= dZ

        x_list.append(r * math.cos(theta))
        y_list.append(r * math.sin(theta))
        z_list.append(z)
    
    return [x_list, y_list, z_list]
    

def main():
    ax = plt.subplot(111, projection='3d')
    ax.grid(True)

    x, y, z = calculateFakeSpiral(10, 1, 2750, 0, 0.015, 0.01)
    ax.plot(x, y, z)

    plt.show()

if __name__ == '__main__':
    main()