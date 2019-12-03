import numpy as np


def herarchy(clusters, K):
    clusters = [np.array(i).reshape(1,2) for i in clusters]
    return doosraherarchy(clusters, K)
    

def doosraherarchy(clusters,K):
    if len(clusters) == K:
        return clusters
    else:
        min = float('inf')
        arg = []
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                cluster1 = clusters[i]
                cluster2 = clusters[j]
                mean1 = cluster1.mean(axis = 0)
                mean2 = cluster2.mean(axis = 0)
                dist = ((mean1 - mean2) ** 2).sum()
                if dist < min:
                    min = dist
                    arg = [i,j]
        new = np.concatenate([clusters[arg[0]], clusters[arg[1]]], axis = 0)
        clusters[arg[0]] = new
        clusters.pop(arg[1])
        return doosraherarchy(clusters, K)
        

