===================================
Visualizing Marker Expression
===================================

### Overview

Visualizing marker gene expression is essential for understanding the biological significance of different cell clusters and their heterogeneity. The application provides multiple visualization options to explore gene expression data effectively.

### Available Plot Types

- **Feature Plot**: Displays the spatial distribution of one or more genes on a UMAP or t-SNE plot, showing expression levels across clusters.
- **Violin Plot**: Illustrates the distribution of gene expression levels within each cluster, helping to understand the variability and expression patterns.
- **Dot Plot**: Represents the average expression levels of selected genes across multiple clusters and conditions. Dot size indicates the percentage of cells expressing the gene in each cluster.
- **Ridge Plot**: Visualizes the distribution of gene expression levels across clusters in a layered fashion, providing a clear view of differences in expression.

### How to Visualize Marker Expression

1. **Select Genes**:  
   Use the dropdown menu to select one or more genes to visualize. You can select multiple genes for comparative visualization in some plot types.

   .. image:: ../_static/images/single_dataset_analysis/visualizing_marker_expression_1.png
      :width: 90%
      :align: center

2. **Choose Plot Type**:  
   Select the desired plot type (Feature Plot, Violin Plot, Dot Plot, or Ridge Plot) to display the expression data.

3. **Customize Plot Settings**:  
   Adjust the settings such as axes labels, text size, and point size to tailor the visualization to your preferences. For Feature Plots, you can also set the minimum and maximum cutoffs for expression levels.

4. **Generate Plot**:  
   Click the corresponding button to generate the plot. For example, click "Display FeaturePlot" for feature plots or "Display VlnPlot" for violin plots.

   .. image:: ../_static/images/single_dataset_analysis/visualizing_marker_expression.png
      :width: 90%
      :align: center

.. tip::  
   Use Feature Plot for spatial visualization of gene expression on dimensional reduction plots (e.g., UMAP, t-SNE). Violin Plot is useful for assessing the distribution and variability of gene expression across clusters.

.. warning::  
   Make sure the genes selected for visualization are relevant to the biological question. Including irrelevant genes can clutter the plot and complicate interpretation.

### Exporting Plots

You can export the generated plots in various formats such as PNG by clicking the "Download" button provided for each plot type.

### Troubleshooting

- **Plot Appears Blank**:  
  Ensure that the selected genes are present in the dataset. Check for correct spelling and gene symbols.

- **Overlapping Clusters in Plots**:  
  Adjust the visualization parameters or try using different plot types to better distinguish between clusters.
