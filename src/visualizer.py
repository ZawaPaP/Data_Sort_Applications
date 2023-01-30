import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import random
from sort_function_for_visualization import insert_sort, bubble_sort, quick_sort, merge_sort
n = 100

for i in range(n):
    data = [random.randint(0,n) for i in range(n)]

generator = bubble_sort(data)
sort_name = "bubble_sort"

cmap = plt.cm.rainbow(np.linspace(0, 1, len(data)))

fig, ax = plt.subplots()

bar_containers = ax.bar(range(len(data)), data, align="edge", color = cmap)

font = {'family':'serif','color':'blue','size':20}
plt.title(sort_name, fontdict = font)
text = ax.text(0.01, 0.95, "", transform = ax.transAxes)

operation = [0]

def animate(A, bar_containers, operation):
    for bar_container, value in zip(bar_containers, A):
        bar_container.set_height(value)

    operation[0] += 1
    text.set_text("operations : {}".format(operation[0]))

anim = FuncAnimation(fig, func=animate, fargs=(bar_containers, operation), frames=generator, interval=30, repeat=False, save_count=100)

#anim.save('tests/{}.gif'.format(sort_name)) 
plt.show()