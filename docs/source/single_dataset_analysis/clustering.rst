==========================
Clustering
==========================

### Overview

Clustering is a key step in single-cell RNA sequencing analysis that groups cells with similar gene expression profiles into clusters. These clusters may correspond to different cell types, states, or other biological distinctions. In this application, clustering is performed in two main steps: **finding neighbors** and **running the clustering algorithm**. Additionally, **UMAP** is used to visualize the clusters.


#### Neighbors Calculation

The first step in clustering is calculating the **nearest neighbors** for each cell. This involves finding cells that are most similar to each other based on their gene expression profiles. In single-cell analysis, this is crucial because cells that are "close" to each other in the expression space are likely to share similar biological functions or states.

- **Why Calculate Neighbors?**  
  Calculating neighbors allows the algorithm to identify groups of cells that are tightly packed in the multidimensional space defined by their gene expression. This is the foundation of clustering, where the idea is that cells with similar profiles form clusters.

- **How Are Neighbors Calculated?**  
  The algorithm uses **Principal Component Analysis (PCA)** to reduce the dimensionality of the data, and then it calculates the nearest neighbors based on the top principal components. You control how many dimensions (principal components) are used, typically between 10 to 20, depending on the complexity of the data.

- **Choice of Dimensions**:  
  Choosing too few dimensions may oversimplify the relationships between cells, while choosing too many may introduce noise and make clustering less accurate. A good starting point is to use between 10 and 20 principal components.

  .. tip::
     Start with 10 principal components, then increase or decrease the number based on how well-separated the clusters appear in the final UMAP plot.

#### UMAP (Uniform Manifold Approximation and Projection)

After finding the nearest neighbors, the **UMAP** algorithm is applied to create a two-dimensional visualization of the data. UMAP preserves both local and global structures in the data, making it ideal for visualizing clusters formed by similar cells.

- **UMAP Visualization**:  
  UMAP generates a low-dimensional plot where each point represents a cell, and the distance between points reflects their similarity in gene expression. Cells that are similar in expression will be closer together, forming clusters.

### Steps to Cluster Cells

1. **Find Neighbors**:  
   Finding neighbors is the first computational step. This establishes which cells are closest to each other based on their expression profiles across the selected number of dimensions.

   - **Number of Dimensions**: Select the number of principal components to use for finding neighbors. This setting directly influences how similarities between cells are computed.
     - More dimensions typically capture more biological variation but can also introduce noise.
     - Start with 10 dimensions and adjust as needed based on the UMAP plot.
   - **Click "Find Neighbors"**: After setting the number of dimensions, click this button to calculate neighbors. A UMAP plot will be generated automatically to visualize the neighbors and potential clusters.

   .. image:: ../_static/images/single_dataset_analysis/neighbors.png
      :width: 90%
      :align: center

2. **Run Clustering**:  
   After neighbors are calculated, the next step is to group cells into clusters. The clustering algorithm works by grouping cells that have similar neighbors into the same cluster.

   - **Resolution**:  
     The resolution parameter controls the size and number of clusters:
     - **High Resolution**: Produces more, smaller clusters.
     - **Low Resolution**: Yields fewer, larger clusters.
     - Start with a resolution of 0.5 and adjust based on the results. Higher values will create more refined clusters, while lower values will create broader groups.
   
   - **Clustering Algorithm**:  
     You can choose between different clustering algorithms, each with unique advantages:
     - **Louvain**: The original algorithm, which is fast and effective for community detection.
     - **Louvain with Multilevel Refinement**: Adds more precision by refining clusters after the initial clustering step.
     - **SLM Algorithm**: Optimized for detecting very fine clusters.
     
     After setting the resolution and algorithm, click **"Find Clusters"** to run the clustering analysis. A new plot showing the clusters will be generated automatically.

   .. image:: ../_static/images/single_dataset_analysis/clustering.png
      :width: 90%
      :align: center

### Visualizing Clusters

- **UMAP Plot**:  
   The UMAP plot is automatically updated after clustering is performed. This plot visualizes the clusters, showing how well the cells separate into distinct groups. Each point represents a cell, and its position relative to others indicates its similarity in gene expression.

   .. tip::
      Use the UMAP plot to assess the quality of clustering. If clusters are overlapping or indistinct, try adjusting the number of dimensions used for neighbors or the resolution parameter for clustering.

- **Cluster Labels**:  
   The clusters are labeled automatically in the UMAP plot. You can further explore each cluster to identify specific cell types or states based on gene expression profiles.

### Common Issues

- **Clusters are not well-separated**:  
   If clusters are not clearly separated in the UMAP plot, try increasing the number of dimensions used to calculate neighbors or lowering the clustering resolution. This can help to capture more variation between cells and improve cluster separation.

- **Too many small clusters**:  
   If you find that there are too many small clusters, try lowering the resolution setting. A lower resolution will merge smaller clusters into larger, more biologically meaningful groups.

- **Neighbor Search Errors**:  
   If an error occurs during the neighbor search, ensure that the input data is properly pre-processed and that you have selected an appropriate number of dimensions for the analysis.

