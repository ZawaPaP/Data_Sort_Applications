import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
from sort_type import SortType, available_sort_type
from sort_function_for_visualization import insert_sort, bubble_sort, quick_sort, merge_sort
from functools import partial
from set_logger import SetLogger
import sys


def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, value in zip(x, y):
        ax.bar(left, value, color = cmap(value))


def update(frame):
    ax.cla() 
    plt.title(sort_name, fontdict = font)
    ax.set(xlim=xlim, ylim=ylim, autoscale_on=False)
    x = range(len(data))
    y = data
    ax.text(0.01, 0.95, "", transform = ax.transAxes).set_text("operations : {}".format(operation[0]))
    gradient_bar(ax, x, y)
    operation[0] += 1

def sort(data, sort_option, start = 0, end=100):
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
cmap = plt.get_cmap('gist_ncar')

fig, ax = plt.subplots()
sort_option = 3
sort_name = SortType(sort_option)
font = {'family':'serif','color':'blue','size':20}

generator = sort(data, sort_option, end = len(data)-1)

xmin, xmax = xlim = 0, n + 1
ymin, ymax = ylim = 0, n + 1
operation = [0]

anim = FuncAnimation(fig, partial(update), frames=generator, interval=15, repeat=False, save_count=3000)
#anim.save('./tests/{}.gif'.format(sort_name))

plt.show()
