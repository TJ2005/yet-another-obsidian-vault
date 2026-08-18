## Clustering Types

### 1. Connectivity (Hierarchical)
models build clusters by linking data points based on distance. They form a tree-like structure called a dendrogram, showing how clusters merge or split. These models don't require the number of clusters in advance. They are useful for visualizing nested groupings and relationships.

- Is an unsupervised machine learning clustering strategy
- Tree like morphologies called dendrograms are used
- Individual data points are located at the bottom
- largest clusters are located at the top
- dendrogram is created by merging or splitting the data points.

#### **Types**

##### **Agglomerative**:

	at every stage we create a dendogram

*Issues with Agglomerative*
- Excessive time and space constraints 
- Matric must be accessed multiple times
- Algorithm is not incremental
- Never undo the merging

#### **Divisive**:

### 2. Centroid models 
represent each cluster by a central point or centroid. Algorithms like k-means fall under this category, where data points are grouped by minimizing the distance to the centroid. These models work well with compact, spherical clusters. They require specifying the number of clusters beforehand.

- non-hierarchical model
- Creates clusters in one step - further iterations refines the clusters formed
- Only usually deals with static sets - it so happens that when new data points  are just inserted in the clusters, it will create a large intra cluster distance and will increase the inertia of the clusters
- suffers from combinatorial

#### **Types**

##### **K Means Algorithm:**

assumes the desired number of cluster k
initial centroids of cluster are randomly chosen

***Issues with k Means Algorithm***
- doesn’t work with categorical data
- doesn't scale well
- choosing k manually
- dependent on initial values of k centroids

**Elbow method (to find the find value of k)**

We take the value of k as a set of values from 1 to 10. It executes the K-means clustering on a given dataset for different values of k

Most Clustering Algorithms
- is memory resident
- don’t scale up to large datasets
- performs I/Os continuously
- Assumes all data to be present at once

Algorithms

- DBSCAN

Characteristics:

1. Require no more than one scan
2. Update results incrementally
3. Works with limited memory
4. Process each tuples only once

### 3. Distribution models 
 assume data is generated from a mixture of statistical distributions. Gaussian Mixture Models (GMMs) are a common example, using probability to assign points to clusters. These models can capture more complex shapes and overlapping clusters. They rely on statistical assumptions about the data.

### 4. Density models 
group data based on regions of high density separated by low-density areas. DBSCAN is a popular algorithm that identifies clusters of arbitrary/irregular shape. These models don't require the number of clusters and can detect noise. They're effective for spatial data and outlier detection.


##  Evaluation Metrics for Clustering
### Inertia:

Sum of distances if all points within a cluster from the centroid of that cluster.

Lesser the inertia value, better are the clusters

### Dunn Index:

It takes into account the distance between the two cluster

Higher the value of the cluster, better are the clusters

### Silhouette Score:

Silhouette Score measures how well a data point fitc s within its cluster compared to others, ranging from -1 to +1. Higher scores indicate better clustering quality.

If the Score is close to 0, it suggests an overlapping cluster