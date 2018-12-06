import utils
import matplotlib.pyplot as plt

points = utils.load_data()

xs, ys = zip(*points)

plt.scatter(xs, ys)
plt.show()
