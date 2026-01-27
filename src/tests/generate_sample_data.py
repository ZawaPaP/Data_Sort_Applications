import numpy as np


n = 1000
data = [i for i in range(n)]
np.random.shuffle(data)
with open("test_input_{}.txt".format(n), mode="w") as fp:
    for x in data:
        fp.writelines(str(x)+'\n')

