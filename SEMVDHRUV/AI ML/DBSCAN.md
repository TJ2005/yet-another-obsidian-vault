A point ( sample )on the graph has a radius. The number of elements in the radius of that circle need to hit a certain threshold to create a cluster.

Every data point is surrounded by a circle with radius $\epsilon$ (epsilon)
- Core Point - if circle that surrounds it has a minimum number of points specified by minPoints parameter.
- Borde point - if the number of points is lower than the minimum required.
- Noise Point - If there are no additional data points in the radius

### Steps
- Algorithm selects a $(x)$ point randomly from he dataset.
- It checks within the radius if there are $\geq \text{minimum points required}$ 
- If yes then it marks 