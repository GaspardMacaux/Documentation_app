# Assigning Cell Identity

## Overview
Assigning cell type identities to clusters is a crucial step in single-cell analysis. This process involves labeling clusters based on known marker gene expression, allowing for the annotation of cell types or states.

## Concept of Cell Type Assignment
Cell type assignment is the process of labeling clusters with known cell type identities based on their gene expression profiles. This step is important for:
- Understanding the composition of cell populations within a dataset
- Relating clusters to known biological cell types or states
- Facilitating downstream analyses such as differential expression or pathway analysis

## Assignment Process

### Marker Gene Identification
Identify marker genes that are characteristic of specific cell types. These genes are highly expressed in certain cell types but not in others.

### Cluster Annotation
Assign cell type identities to clusters based on the expression patterns of marker genes. This can be done manually by renaming clusters in the UI or through automated tools that match expression patterns to reference datasets.

![](../_static/images/multiple_datasets_analysis/assigning_cell_identity_merge.png)

## Using the Interface

### UMAP Visualization
Visualize the clusters in a UMAP plot to identify the spatial distribution of cells.

### Cluster Management
1. **Rename Clusters**:
   - Select a cluster from the dropdown menu
   - Input a new name to rename the cluster
   - Use the "Rename Cluster" button to apply changes
2. **Merge Clusters**:
   - Select a cluster and input another cluster name to merge
   - Use the "Merge Clusters" button to combine selected clusters

### Visual Customization
1. **Update Cluster Colors**:
   - Use color picker for cluster selection
   - Set desired color for each cluster
   - Apply changes with "Update Color" button
2. **Export Options**:
   - Download UMAP plot after assignments
   - Save for further analysis or presentation