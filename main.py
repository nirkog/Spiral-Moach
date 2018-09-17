import math
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    # r, theta, a, b, phi = sp.symbols('r, theta, a, b, phi')
    # d_pitch = 15
    # pitch = d_pitch / 180 * math.pi
    # phi = math.pi / 2 - pitch
    # a = 0.1
    # b = 1 / math.tan(phi)
    # r = sp.Lambda(theta, a * sp.exp(b * theta))
    # r_diff = sp.diff(r(theta), theta)
    
    # print("Calculating Spiral With a " + str(d_pitch) + " degrees Pitch!")

    # r_list = []
    # theta_list = []
    # x_list = []
    # z_list = []
    # y_list = []

    # theta_list.append(-5 * math.pi / 180)
    # r_list.append(r(theta_list[0]))

    # x_list.append(r_list[0] * math.cos(theta_list[0]))
    # y_list.append(r_list[0] * math.sin(theta_list[0]))
    # z_list.append(0)

    # iterations = 7 * 180
    # step_size = math.pi / 180
    # z_inc = 0.1

    # for i in range(0, iterations):
    #     c_theta = theta_list[i] + step_size
    #     c_r = r(c_theta)
    #     c_x = c_r * math.cos(c_theta)
    #     c_y = c_r * math.sin(c_theta)
    #     c_z = z_list[i] + z_inc

    #     theta_list.append(c_theta)
    #     r_list.append(c_r)
    #     x_list.append(c_x)
    #     y_list.append(c_y)
    #     z_list.append(c_z)
    
    # ax = plt.subplot(111, projection='3d')

    # ax.plot(x_list, y_list, z_list)
    # ax.grid(True)
    
    # plt.show()

    r_list = []
    theta_list = []
    z_list = []

    realR_list = []

    pitch = 10 / 180 * math.pi
    phi = math.pi / 2 - pitch

    a = 1
    b = 1 / math.tan(phi)

    theta = 5
    r = a * math.exp(b * theta)
    z = 0

    theta_list.append(theta)
    r_list.append(r)
    z_list.append(z)
    realR_list.append(r)

    dTheta = 0.015
    z_step = 0.0005

    x_list = []
    y_list = []

    x_list.append(r * math.cos(theta))
    y_list.append(r * math.sin(theta))

    for i in range(10000):
        theta += dTheta
        z += z_step
        r = (math.sin(phi) / math.sin(phi + dTheta)) * r

        theta_list.append(theta)
        z_list.append(z)
        r_list.append(r)
        realR_list.append(a * math.exp(b * theta))

        x_list.append(r * math.cos(theta))
        y_list.append(r * math.sin(theta))

    # ax = plt.subplot(111, projection='polar')
    # ax.plot(theta_list, r_list)
    # ax.set_title("FAKE!")

    # plt.figure()

    bx = plt.subplot(111, projection='3d')
    bx.plot(x_list, y_list, z_list)
    bx.set_title("FAKE!")

    #plt.figure()

    plt.show()

if __name__ == '__main__':
    main()