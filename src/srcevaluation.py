import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

def k_distance_plot(X, k=10):
    """
    Plot k-distance graph for DBSCAN epsilon selection.
    Mirrors notebook intent.
    """
    nn = NearestNeighbors(n_neighbors=k)
    nn.fit(X)
    distances, _ = nn.kneighbors(X)
    k_dist = np.sort(distances[:, -1])

    plt.figure()
    plt.plot(k_dist)
    plt.xlabel("Points (sorted)")
    plt.ylabel(f"{k}-NN distance")
    plt.title("k-Distance Plot (for DBSCAN eps selection)")
    plt.show()
