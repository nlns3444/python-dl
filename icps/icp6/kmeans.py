import pandas#importing the dataset in csv format
import pylab as pl#pylab is the graphing library
from sklearn.cluster import KMeans#sklearn is used to devise the clustering algorithm.
from sklearn.decomposition import PCA
variables = pandas.read_csv(r'/Users/nlns/Downloads/Python_Lesson6/sample_stocks.csv')#stores the dataset into variables
Y = variables[['returns']]
X = variables[['dividendyield']]
Nc = range(1, 20)#number of clusters in the range of 1,20

kmeans = [KMeans(n_clusters=i) for i in Nc]# Additionally, we are also normalizing the data in order to make it suitable for analysis with PCA

kmeans

score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]

score

pl.plot(Nc,score)

pl.xlabel('Number of Clusters')

pl.ylabel('Score')

pl.title('Elbow Curve')

pl.show()

pca = PCA(n_components=1).fit(Y)

pca_d = pca.transform(Y)

pca_c = pca.transform(X)
kmeans=KMeans(n_clusters=3)

kmeansoutput=kmeans.fit(Y)

kmeansoutput

pl.figure('3 Cluster K-Means')

pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)

pl.xlabel('Dividend Yield')

pl.ylabel('Returns')



pl.show()