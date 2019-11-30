import numpy as np
from kmeans import kmeans


def divisive(clusters,K):
    clusters = [np.array(clusters)]
    return doosradivisive(clusters,K)
    

def doosradivisive(clusters,K):
    if len(clusters) == K:
        return clusters
    else:
        ls = [0 for i in range(len(clusters))]
        n = 0
        for i in clusters:
            ls[n] = i.mean(axis = 0)
            n += 1
        dist = [0 for i in range(len(clusters))]
        largest = 0
        
        for j in range(len(ls)):
            a = ((ls[j] - clusters[j])**2)
            a = a.sum(axis = 1)
            a = a.mean(axis = 0)
            dist[j] = a
            if dist[j] > dist[largest]:
                largest = j
        k = kmeans(clusters[largest],2)
        clusters[largest] = k[0]
        clusters.append(k[1])
        return doosradivisive(clusters,K)
    
