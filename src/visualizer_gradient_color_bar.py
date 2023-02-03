import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
from sort_type import SortType, available_sort_type
from sort_function_for_visualization import insert_sort, bubble_sort, quick_sort, merge_sort
from functools import partial
from set_logger import SetLogger
import sys


def gradient_image(ax, extent, direction=0, cmap_range=(0, 1), **kwargs):
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max()*X
    im = ax.imshow(X, extent=extent, interpolation='bicubic', norm = plt.cm.colors.NoNorm(vmin = 0, vmax = 1), **kwargs)
    return im

def gradient_bar(ax, x, y, width=0.5, bottom=0):
    n = len(x)
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top), cmap=plt.cm.get_cmap('rainbow'), cmap_range=(0, top/n))

def update(frame):
    ax.cla() 
    ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
    plt.title(sort_name, fontdict = font)
    x = range(len(data))
    y = data
    ax.text(0.01, 0.95, "", transform = ax.transAxes).set_text("operations : {}".format(operation[0]))
    gradient_bar(ax, x, y)
    operation[0] += 1

def sort(data, sort_option, start = 0, end = 100):
    logger = SetLogger().set_logger(__name__)
    try:
        if sort_option == SortType.INSERT.value:
            return insert_sort(data)
        elif sort_option == SortType.MERGE.value:
            return merge_sort(data, start, end)
        elif sort_option == SortType.QUICK.value:
            return quick_sort(data, start, end)
        elif sort_option == SortType.BUBBLE.value:
            
            return bubble_sort(data)
    except UnboundLocalError as e:
        logger.info(e)
        logger.info('sort_option: ' + str(sort_option))
        available_sort_type()
        sys.exit(1)

n = 100
# 重複データが出ないように変更
data = [i for i in range(1,n+1)]
np.random.shuffle(data)

fig, ax = plt.subplots()
sort_option = 4
sort_name = SortType(sort_option)

generator = sort(data, sort_option, end = len(data))

font = {'family':'serif','color':'blue','size':20}

xmin, xmax = xlim = 0, n + 1
ymin, ymax = ylim = 0, n + 1
operation = [0]

anim = FuncAnimation(fig, partial(update), frames=generator, interval=15, repeat=False, save_count=100)

plt.show()
