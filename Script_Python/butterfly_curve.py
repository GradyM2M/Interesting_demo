# import matplotlib.pyplot as plt
# import math
#
# thetas = []  # 用来存放极角
# rhos = []  # 用来存放极径
#
# for i in range(-180, 180):
#     theta = i*math.pi/180  # 角度转弧度
#     rho = math.exp(math.cos(theta)) - 2*math.cos(4*theta)+math.pow(math.sin(theta/12), 5)  # 极径
#     thetas.append(theta)
#     rhos.append(rho)
#
# fig = plt.figure()  # 新建画布
# plt.polar(thetas, rhos, color="red")  # 极坐标画图
# plt.title("Butter Curve")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import math

X = []
Y = []
theta = 0

for theta in np.linspace(0, math.pi*12, 10001):
    x = math.cos(theta)*(math.exp(math.cos(theta)) - 4*math.cos(4*theta) + math.pow(math.sin(theta/4), 5))
    y = 1.5*math.sin(theta)*(math.exp(math.cos(theta)) - 4*math.cos(4*theta) + math.pow(math.sin(theta/4), 5))
    X.append(x)
    Y.append(y)

fig = plt.figure()  # 新建画布
plt.plot(Y, X, color="red", linewidth=1)  # 极坐标画图
plt.title("butterfly")
plt.show()
