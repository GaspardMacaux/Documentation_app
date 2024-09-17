==========================
Dimensional Reduction
==========================

### Overview

Dimensional reduction is a crucial step in simplifying high-dimensional single-cell RNA sequencing data, making it easier to analyze and interpret. In this application, **Principal Component Analysis (PCA)** is the sole technique used for dimensional reduction, followed by an **Elbow Plot** to help determine the number of principal components (PCs) to retain.

### Why PCA?

**PCA** is chosen for several reasons:

- **Simplicity and Speed**: PCA is computationally efficient and scales well with large datasets.
- **Interpretability**: PCA linearly reduces the data, making the principal components easy to interpret in terms of variance explained by each component.
- **Initial Dimensional Reduction**: PCA is often used as the first step before further downstream analyses like clustering.

### How to Perform Dimensional Reduction

1. **Scale the Data & Perform PCA**:  
   In this application, scaling the data and running PCA are combined into a single operation.

   - Click **"Scale Data & PCA"** to perform both steps simultaneously.
   - **Scaling**: The data is scaled so that the mean expression of each gene across all cells is 0, and the variance is 1. This prevents genes with higher expression from dominating the PCA.
   - **PCA**: After scaling, PCA is automatically performed. The principal components are computed, capturing the maximum variance in the dataset.

2. **View PCA Results and Plots**:  
   Once PCA is complete, the results and corresponding plots are automatically displayed:
   - **PCA Results**: A summary of the principal components is shown, including how much variance each component explains.
   - **Dimensional Loading Plot**: This plot displays the loadings of the principal components, helping you understand the contribution of individual genes to the principal components.
   - **PCA Plot**: A scatter plot of the top principal components, showing how the cells are distributed across the principal components.

   .. image:: ../_static/images/single_dataset_analysis/dimensional_reduction.png
      :width: 90%
      :align: center


3. **Elbow Plot**:  
   After PCA, the **Elbow Plot** is used to determine the optimal number of components to retain. The Elbow Plot shows how much variance is explained by each component, with the "elbow" indicating the point where adding more components yields diminishing returns.

   The plot is generated automatically when PCA is complete, and no additional button is needed to trigger it.

   .. image:: ../_static/images/single_dataset_analysis/elbow_plot.png
      :width: 90%
      :align: center

.. tip::
   PCA is a fast and effective technique for reducing the dimensionality of large datasets. Use the Elbow Plot to determine how many components to retain for further analysis.

.. warning::
   Retaining too few components can lead to oversimplification, while retaining too many may introduce noise. For single-cell RNA sequencing data, retaining between 10 and 20 principal components is generally recommended.


### Common Issues

- **Error During Data Scaling**:  
   Ensure that the input data is correctly formatted and contains valid gene names before performing scaling and PCA. If an error occurs during scaling, it is typically due to improperly formatted data.

- **Variance Explained by PCA is Too Low**:  
   If the variance explained by the top principal components is too low, you may need to examine the dataset quality or increase the number of components. Using too few components may lead to an oversimplified analysis.
