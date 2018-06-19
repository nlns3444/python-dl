import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.cluster import KMeans
# load a dataset of height in  inches and weight in pounds of a person into an array
X = np.array( [[5,35], [6,15],[5,102], [5,100], [30,145],[8,170], [5,80], [6,178],[5,152], [4,100], [5,145],[8,170], [7,80], [6,78],[6,62], [4,50], [55,145],[65,78], [71,130], [60,78],[55,32], [42,40], [30,45],[85,70], [71,80], [6,8],[45,52],[80,91],] )
# plot them on the graph
plt.scatter(X[:,0],X[:,1], label='True Position')
plt.show()
# took 4 clusters for S, M, L, XL size in tshirt and fit the data in X array
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
# show to which clusters they belong
print(kmeans.cluster_centers_)
# print the labels
print(kmeans.labels_)
plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
# show datapoints belonging to each centroid in different colors on the graph
plt.show()
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.show()
# show centroids on the graph in black color
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.show()