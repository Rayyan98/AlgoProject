import numpy as np
# float_formatter = lambda x: "%.3f" % x
#np.set_printoptions(formatter={'float_kind':float_formatter})
from sklearn.datasets.samples_generator import make_circles
from sklearn.cluster import SpectralClustering, KMeans
from sklearn.metrics import pairwise_distances
from matplotlib import pyplot as plt
import pandas as pd
import networkx as nx
import seaborn as sns
#sns.set()


# def draw_graph(G):
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G, pos)
    # nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    # plt.show()


def spectral(points, k):
    X = np.array(points)
    sc = SpectralClustering(n_clusters=k, affinity='nearest_neighbors')
    sc_clustering = sc.fit(X)
    points = np.array(points)
    lis = []
    labels = np.array(sc.labels_)
    for i in range(k):
        lis.append(points[labels == i, :])
    return lis
    
    
    


