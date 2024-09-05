===============================
Heat Maps & Dual Expression
===============================

### Overview

Heat maps provide a visual representation of gene expression levels across different clusters. Dual expression analysis allows the exploration of co-expression patterns between two genes.

### Creating Heat Maps

1. **Select Genes for Heatmap**: Choose genes from the dropdown menu to include in the heatmap.
2. **Customize Heatmap Settings**:
   - **Cluster Rows/Columns**: Enable clustering to group similar genes or samples.
   - **Color Scaling**: Adjust color scales to enhance visibility.
3. **Generate Heatmap**: Click "Generate Heatmap" to visualize the expression patterns.

.. tip::
   Selecting a limited number of highly variable genes for heatmap visualization can make patterns more evident and easier to interpret.

### Dual Expression Analysis

1. **Select Genes for Dual Expression**: Choose two genes to analyze their co-expression patterns.
2. **Run Dual Expression Analysis**: Click "Run Dual Expression" to generate the plot.

.. warning::
   Heat maps with too many genes can become cluttered and hard to interpret. Consider filtering genes based on variance or biological relevance.

### Common Issues

- **Heatmap is too dense**: Reduce the number of genes visualized or increase the clustering granularity.
- **Dual expression plot shows no pattern**: Ensure that the selected genes are co-expressed and relevant to the analysis.
