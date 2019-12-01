import matplotlib.pyplot as plt
import numpy as np


def visualize(clusters, **kwargs):
    for i in clusters:
        plt.scatter(i[:,0], i[:,1], **kwargs)
    plt.show()
    

def generatePoints(n, k):
    width = n / 10
    sd = width / 4
    lis = []

    sectors = np.random.choice(range(k ** 2), k, replace = False)

    for i in sectors:
        num_p = ( 0.5 + np.random.random() * 0.5) * n 
        for j in range(int(num_p)):
            x_num = i % k
            y_num = i // k
            x_mid = x_num * width + width / 2
            y_mid = y_num * width + width / 2
            
            p = [np.random.normal(x_mid, sd), np.random.normal(y_mid, sd)]
            lis.append(p)

    np.random.shuffle(lis)
    return lis


