import numpy as np


def kmeans(points, K):
    clusters = []
    
    centroids = np.zeros((K, 2)) # nparrays that will contain coordinates of centroid in each row
    
    random_index = np.random.choice(range(len(points)), K, replace = False)
    for i in range(len(random_index)):
        centroids[i, :] = points[random_index[i]]

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

    clusters = [np.array(i) for i in clusters]
    return clusters


