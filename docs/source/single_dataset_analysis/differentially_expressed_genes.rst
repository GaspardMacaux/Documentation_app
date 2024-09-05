===========================================
Differentially Expressed Genes (DEGs)
===========================================

### Overview

Identifying differentially expressed genes (DEGs) helps understand the differences between clusters or experimental conditions.

### How to Identify DEGs

1. **Select Clusters for Comparison**: Choose the clusters to compare from the dropdown menu.
2. **Set DEG Parameters**:
   - **Log Fold Change Threshold**: Set the minimum log fold change to identify significant DEGs.
   - **Percentage Threshold**: Set the minimum percentage of cells expressing the gene in either cluster.

3. **Run DEG Analysis**: Click "Find DEGs" to perform the analysis.

.. tip::
   A log fold change threshold of 0.25 and a minimum percentage of 10% are good starting points, but these can be adjusted based on the dataset's characteristics.

.. warning::
   Very low thresholds may produce too many false positives, while very high thresholds may miss important DEGs. Adjust parameters carefully.

### Common Issues

- **No DEGs found**: Lower the log fold change threshold or increase the minimum percentage of cells.
- **Too many DEGs**: Increase the log fold change threshold to focus on more significant changes.

### Visualizing DEGs

- **Volcano Plot**: Use the volcano plot to visualize DEGs based on their significance and log fold change.
- **Heatmap**: Create heatmaps to display the expression patterns of the top DEGs across clusters.
