import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

points = 100000



rand = np.random.uniform(-1, 1, 2 * points)
rand_points = rand.reshape(points, 2)
norm_points = rand_points[:, 0] ** 2 + rand_points[:, 1] ** 2
points_inside = rand_points[norm_points < 1]
points_outside = rand_points[norm_points > 1]
# print(len(points_inside))
# volume = 8*len(points_inside)/points
pi_approx = 4 * len(points_inside) / points

print(pi_approx)

fig = plt.figure()  # creating the figure(canvas) on which you can add one or more subplots(axes).
ax = fig.add_subplot(111, aspect='equal')  # adding axes to the figure
rectangle = patches.Rectangle((-1, -1), 2, 2, facecolor='none', edgecolor='black')
circle = patches.Circle((0, 0), 1, facecolor='none', edgecolor='black')
ax.add_patch(rectangle)  # ax.add_patch(rectangle) adds the rectangle patch created above to the axes.
ax.add_patch(circle)
plt.xlim([-1.1, 1.1])
plt.ylim([-1.1, 1.1])
plt.scatter(points_inside[:, 0], points_inside[:, 1], color='green', s=0.05)
plt.scatter(points_outside[:, 0], points_outside[:, 1], color='red', s=0.05)

plt.show()

