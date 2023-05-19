import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 读取第一个CSV文件的数据
z_data = []
x_data = []
y_data = []

with open('YEILD SURFACE.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        z, x, y = map(float, row)
        z_data.append(z)
        x_data.append(x)
        y_data.append(y)
x_data, y_data = np.meshgrid(x_data, y_data)
z_data = np.array(z_data)
x_data = np.array(x_data)
y_data = np.array(y_data)

num_groups = len(PeZ) // int(MStep + 1)

# 重新整理数据，使每一组数据成为一个单独的实体
x_data_grouped = x_data.reshape(num_groups, int(MStep + 1))
PeY_grouped = PeY.reshape(num_groups, int(MStep + 1))
PeZ_grouped = PeZ.reshape(num_groups, int(MStep + 1))

# 创建一个三维图形对象
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制第一个三维面图
ax.plot_surface(x_data, y_data, z_data, cmap='viridis', edgecolor='none')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# # 读取第二个CSV文件的数据
# z_data_2 = []
# x_data_2 = []
# y_data_2 = []
#
# with open('Section 1_FullYieldSurface.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=' ')
#     for row in reader:
#         z, x, y = map(float, row)
#         z_data_2.append(z)
#         x_data_2.append(x)
#         y_data_2.append(y)
# x_data_2, y_data_2 = np.meshgrid(x_data_2, y_data_2)
# z_data_2 = np.array(z_data_2)
# x_data_2 = np.array(x_data_2)
# y_data_2 = np.array(y_data_2)
# # 绘制第二个三维面图
# ax.plot_surface(x_data_2, y_data_2, z_data_2, cmap='viridis', edgecolor='none')

# 显示图形
plt.show()
