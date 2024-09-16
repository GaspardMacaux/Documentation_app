==============================
Subset
==============================

### Overview

Subsetting allows users to focus on specific clusters or genes of interest by creating a smaller dataset that includes only the selected cells or genes.

### How to Create a Subset

1. **Select Clusters or Genes**: Choose clusters or genes to include in the subset.
2. **Apply Subset**: Click "Apply Subset" to create a new dataset with the selected cells or genes.

.. image:: ../_static/images/single_dataset_analysis/subset.png
   :width: 90%
   :align: center

.. tip::
   Subsetting can help in reducing computational load and focusing on specific biological questions.

.. warning::
   Subsetting may lead to loss of important data if not done carefully. Ensure that the subset still contains sufficient data for meaningful analysis.

### Visualizing Subsets

- **UMAP/t-SNE Plot**: Visualize the subset to confirm the correct selection of cells or genes.

### Common Issues

- **Subset is too small**: Ensure that enough cells or genes are included for meaningful analysis.
- **Loss of biological diversity**: Verify that the subset represents the full biological diversity of the original dataset.
