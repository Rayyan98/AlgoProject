from visulaize import visualize, generatePoints, generatePoints2
from kmeans import kmeans
from divisor import divisive
from GMM import mixtureModel
from numpy.random import seed as seed
from matplotlib import pyplot as plt
from spectral import spectral
from herarchical import herarchy
import time


print("Starting .. ")

seed(7)



def noteTime(number_points, clusters, visual = False):
    p = generatePoints(number_points, clusters)
    times = []
    
    for i in functions:
        start = time.time()
        cluster_result = i(p, clusters)
        times.append(time.time() - start)
        if visual:
            visualize(cluster_result)
  
    return times


# testcases = [[10, 3], [20, 3], [50, 3], [100, 3]]
# functions = [kmeans, divisive, mixtureModel, spectral, herarchy]

# testcases = [[100, 2], [200, 2], [500, 2], [1000, 2], [5000, 2], [10000, 2], [20000, 2]]
# functions = [kmeans, divisive, mixtureModel, spectral]

# testcases = [[i, 2] for i in range(20, 201, 5)]
# functions = [kmeans, divisive, mixtureModel, spectral]

# testcases = [[20, 2]]
# functions = [kmeans, divisive, mixtureModel, spectral, herarchy]

# testcases = [[500, 2]]
# functions = [kmeans, divisive, mixtureModel, spectral]

# testcases = [[100, 8]]
# functions = [kmeans, divisive, mixtureModel, spectral]

# testcases = [[5, 20]]
# functions = [kmeans, divisive, mixtureModel, spectral, herarchy]

seed(6)
testcases = [[30, 2]]
functions = [kmeans, divisive, mixtureModel, spectral]


test_times = []
for number_points, clusters in testcases:
    print(number_points, clusters)
    times = noteTime(number_points, clusters, True)
    test_times.append(times)
    # print(times)


total_points = [i * j for i,j in testcases]

times_seq = list(zip(*test_times))


for i, name in zip(times_seq, functions):
    plt.scatter(total_points, i)
    plt.plot(total_points, i, label = str(name).split()[1])

plt.legend()
plt.show()

