import numpy as np


def kmeans(points, K):
    clusters = []
    
    dim = len(points[0]) # find numbers of features in each points
    centroids = np.zeros((K, dim)) # nparrays that will contain coordinates of centroid in each row
    random_points = np.random.sample(points, K)
    centroids[:,:] = random_points # initialize centroid with random points
    change = True  # denotes if any centroid has changed significantly
    iteration = 0

    while change and iteration < 20:
        iteration += 1
        clusters=[[] for i in range(K)]
        
        for i in points: # find centroid nearest to each point and assign to cluster
            differences = centroids - i
            differences = differences ** 2

            assert (differences < 0).sum() == 0
            distances = differences.sum(axis = 1)
            closest = distances.argmin()
            clusters[closest].append(i)

        change = False
        for i in range(len(clusters)): # calcualte new centroid of each cluster
            center = np.array(clusters[i]).mean(axis = 0)
            if ((centroids[i, :] - center) ** 2).sum() > 0.16: # check if centroid has changed significantly
                change = True
            centroids[i, :] = center
                    
    return clusters


