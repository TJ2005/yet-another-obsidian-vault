## K-Means Clustering

## 1. Definition

- **K-Means** is an unsupervised machine learning algorithm used to group data points into _k_ clusters.
- Each cluster is represented by its **centroid** (mean of points in the cluster).
- The algorithm minimizes the **within-cluster sum of squares (WCSS)**, also known as inertia.

---

## 2. Working of the Algorithm

1. **Choose k**: Decide the number of clusters (_k_).
2. **Initialize centroids**: Randomly select _k_ points as initial centroids.
3. **Assign points**: Each data point is assigned to the nearest centroid (using Euclidean distance or other metrics).
4. **Update centroids**: Recalculate centroids as the mean of all points in each cluster.
5. **Repeat**: Steps 3–4 are repeated until centroids stabilize or a maximum number of iterations is reached.
6. **Convergence**: The algorithm stops when assignments no longer change or the cost function stabilizes.

---

## 3. Objective Function

The goal is to minimize:

$$ J = \sum_{i=1}^{k} \sum_{x \in C_i} | x - \mu_i |^2 $$

Where:

- $C_i$ = cluster i
- $\mu_i$ = centroid of cluster i
- $x$ = data point

---

## 4. Choosing k (Number of Clusters)

- **Elbow Method**: Plot WCSS vs. k and choose the point where the curve bends.
- **Silhouette Score**: Measures cohesion and separation of clusters.
- **Gap Statistic**: Compares WCSS with a reference null distribution.

---

## 5. Advantages

- Simple and easy to implement.
- Efficient for large datasets.
- Works well when clusters are spherical and equally sized.
- Fast convergence compared to hierarchical clustering.

---

## 6. Limitations

- Requires pre-specifying _k_.
- Sensitive to initialization (different runs may yield different results).
- Struggles with non-spherical clusters or clusters of varying density.
- Sensitive to outliers (they can distort centroids).
- Assumes continuous numerical features (categorical data requires adaptations like k-modes).

---

## 7. Variants

- **K-Means++**: Improves centroid initialization to reduce poor clustering.
- **Mini-Batch K-Means**: Uses small random batches for faster computation on large datasets.
- **Kernel K-Means**: Extends to non-linear cluster boundaries using kernel functions.

---

## 8. Applications

- **Customer Segmentation**: Grouping customers by purchasing behavior.
- **Image Compression**: Reducing colors in an image by clustering pixel values.
- **Document Clustering**: Organizing text documents into topics.
- **Anomaly Detection**: Identifying outliers as points far from any centroid.
- **Market Basket Analysis**: Grouping products based on co-purchase patterns.

---

## 9. Best Practices

- Scale features before applying K-Means (standardization or normalization).
- Run multiple times with different initializations to avoid local minima.
- Use dimensionality reduction (PCA, t-SNE) before clustering high-dimensional data.
- Validate clusters using silhouette scores or domain knowledge.
