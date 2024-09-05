===================================
Visualizing Marker Expression
===================================

### Overview

Visualizing gene expression markers is crucial for interpreting the biological significance of clusters and understanding cellular heterogeneity.

### Available Plot Types

- **Feature Plot**: Visualizes the expression of one or more genes across clusters on a UMAP or t-SNE plot.
- **Violin Plot**: Displays the distribution of gene expression levels for different clusters.
- **Dot Plot**: Represents gene expression levels across multiple clusters and conditions.
- **Heatmap**: Shows the expression levels of selected genes across clusters.

### How to Visualize Marker Expression

1. **Select Genes**: Use the dropdown menu to select one or more genes to visualize.
2. **Choose Plot Type**: Select the desired plot type (Feature Plot, Violin Plot, Dot Plot, or Heatmap).
3. **Customize Plot Settings**: Adjust settings such as axes labels, text size, and point size.
4. **Generate Plot**: Click the "Run Visualization" button to generate the plot.

.. tip::
   Use Feature Plot for spatial visualization and Violin Plot for assessing the distribution of gene expression levels across clusters.

.. warning::
   Make sure the genes selected for visualization are relevant to the biological question. Including irrelevant genes can clutter the plot and make interpretation challenging.

### Exporting Plots

You can export plots in various formats (PNG, PDF) by clicking the "Download" button.

### Troubleshooting

- **Plot appears blank**: Ensure that the selected genes are present in the dataset.
- **Overlapping clusters**: Adjust the visualization parameters or try a different dimensional reduction method.
