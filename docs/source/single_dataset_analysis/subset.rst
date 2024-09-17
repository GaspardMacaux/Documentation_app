===============================
Subset
===============================

### Overview

Subsetting allows users to focus on specific clusters or genes of interest by creating a smaller dataset that includes only the selected cells or genes. This can help streamline the analysis by reducing computational load and focusing on specific biological questions.

### How to Create a Subset

#### Subset by Clusters

1. **Select Clusters**:  
   Choose the clusters to include in the subset using the dropdown menu. Multiple clusters can be selected simultaneously.

2. **Apply Subset**:  
   Click "Apply cluster based subset" to create a new dataset containing only the selected clusters.

.. image:: ../_static/images/single_dataset_analysis/subset.png
   :width: 90%
   :align: center

#### Subset by Gene Expression

1. **Enter Gene List**:  
   Input a comma-separated list of genes to use for subsetting.

2. **Set Expression Threshold**:  
   Specify an expression threshold. Cells will be included in the subset if they express at least a certain number of genes from the list at or above this threshold.

3. **Apply Gene Subsetting**:  
   Click "Apply Gene Subsetting" to create a subset based on the specified gene expression criteria.

### Visualizing Subsets

- **UMAP Plot**:  
  - **Global UMAP**: Shows the UMAP plot for the entire dataset before subsetting.
  - **Subset UMAP**: Displays the UMAP plot for the subsetted dataset to confirm the correct selection of cells or genes.

### Downloading the Subset

- After applying the subset, you can download the new subsetted Seurat object by clicking "Save subset as .RDS".

.. tip::  
   Subsetting can help reduce computational load and focus on specific biological questions. However, careful consideration is required to ensure the subset still captures the essential biological diversity of the dataset.

.. warning::  
   Subsetting may lead to loss of important data if not done carefully. Ensure that the subset contains sufficient cells or genes for meaningful analysis.

### Common Issues

- **Subset is too small**:  
   If the resulting subset is too small, ensure that enough clusters or genes are included to retain a meaningful sample size.

- **No cells found with the selected identities**:  
   Ensure that the selected clusters or genes exist in the dataset and that the expression threshold is set appropriately.

- **Loss of biological diversity**:  
   Verify that the subset still represents the full biological diversity necessary for your analysis objectives.
