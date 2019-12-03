import math
from visulaize import *
import numpy as np
from kmeans import kmeans
from sklearn.datasets import make_spd_matrix
from scipy.stats import multivariate_normal
import random

def mixtureModel(points, k):
    eps=1e-8
    means = np.array(random.sample(points, k))
    weights = np.array(np.ones((k)) / k)
    cova = []
    for i in range(k):
        cova.append(make_spd_matrix(2))
    for i in range(40):
        probs = []
        for j in range(k):
            probs.append(multivariate_normal.pdf(points, means[j],cova[j], allow_singular = True))
        probs = np.array(probs)
        new = []
        for j in range(k):
            new.append((probs[j] * weights[j]) / (np.sum([probs[i] * weights[i] for i in range(k)], axis=0)+eps))
        
            means[j] = np.sum(new[j].reshape(len(points),1) * points, axis=0) / (np.sum(new[j]+eps))
            cova[j] = np.dot((new[j].reshape(len(points),1) * (points - means[j])).T, (points - means[j])) / (np.sum(new[j])+eps)
            weights[j] = np.mean(new[j])
    probs = []
    for j in range(k):
        probs.append(multivariate_normal.pdf(points, means[j],cova[j], allow_singular = True))
    probs = np.array(probs)
    pred = np.argmax(probs, axis=0)
    clus = []
    for i in range(k):
        pred_ids = np.where(pred == i)[0]
        clus.append(np.array([points[j] for j in pred_ids]))
    return clus
    
        