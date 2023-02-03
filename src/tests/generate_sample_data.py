import random


n = 100000
data = [random.randint(0,n) for i in range(n)]
with open("test_input_{}.txt".format(n), mode="w") as fp:
    for x in data:
        fp.writelines(str(x)+'\n')

