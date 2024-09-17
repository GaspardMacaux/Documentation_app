==========================
Assigning Cell Identity
==========================

### Overview

Assigning cell type identities to clusters is a crucial step in single-cell analysis. This process involves labeling clusters based on known marker gene expression, allowing for the annotation of cell types or states.

### Concept of Cell Type Assignment

Cell type assignment is the process of labeling clusters with known cell type identities based on their gene expression profiles. This step is important for:

- Understanding the composition of cell populations within a dataset.
- Relating clusters to known biological cell types or states.
- Facilitating downstream analyses such as differential expression or pathway analysis.

### How to Assign Cell Type Identities

1. **Marker Gene Identification**:  
   Identify marker genes that are characteristic of specific cell types. These genes are highly expressed in certain cell types but not in others.

2. **Cluster Annotation**:  
   Assign cell type identities to clusters based on the expression patterns of marker genes. This can be done manually by renaming clusters in the UI or through automated tools that match expression patterns to reference datasets.

3. **Metadata Update**:  
   Update the Seurat object metadata to reflect the new cell type identities, which can then be used in further analyses.

.. image:: ../_static/images/multiple_datasets_analysis/assigning_cell_identity_merge.png
   :width: 90%
   :align: center

### How to Use the Interface

1. **UMAP Plot**:  
   Visualize the clusters in a UMAP plot to identify the spatial distribution of cells.

2. **Rename Clusters**:  
   - Select a cluster from the dropdown menu and input a new name to rename the cluster.
   - Use the "Rename Cluster" button to apply the changes.

3. **Merge Clusters**:  
   - If two clusters need to be merged, select a cluster and input the name of another cluster to merge them.
   - The interface allows merging by selecting the clusters and using the "Merge Clusters" button.

4. **Update Cluster Colors**:  
   Customize the colors of clusters for better visualization in plots. Use the color picker and "Update Color" button to set the desired color for each cluster.

5. **Download UMAP Plot**:  
   After assigning identities, download the updated UMAP plot for further use.

### Comparison and Differential Expression Analysis

- **Differential Expression within a Cluster**:  
  Compare one cluster with all others to identify differentially expressed genes. Adjust the log fold change and percentage thresholds to refine the analysis.

- **Cluster Comparison**:  
  Compare gene expression between two specific clusters or between the same cluster across different datasets.

- **Cluster Table Generation**:  
  Generate and view a table that provides an overview of clusters with their assigned identities.

.. tip::  
   Use multiple marker genes to increase the accuracy of cell type assignment. Validate assignments with known biological information and reference datasets.

.. warning::  
   Misidentification of cell types can lead to incorrect conclusions. Always cross-validate assigned identities with additional data or literature.

### Applications

- **Cell Type Profiling**:  
  Understand the diversity of cell types within a dataset.

- **Comparative Studies**:  
  Compare cell type compositions across different conditions or experimental setups.
