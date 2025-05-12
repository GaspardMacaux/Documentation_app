# Visualizing Gene Expression

## Overview
Visualizing gene expression is an essential step in understanding the distribution and variability of specific genes across different cell populations. This section provides various visualization tools to explore gene expression in your integrated datasets.

## Types of Plots Available

### Feature Plot
Displays the spatial expression of genes on a UMAP or PCA plot. Useful for visualizing gene co-expression and identifying marker genes for specific clusters.

### Violin Plot
Shows the distribution of gene expression levels across different clusters. Useful for comparing gene expression between clusters and identifying marker genes.

### Dot Plot
Represents the expression of multiple genes across clusters. Each dot's size represents the percentage of cells expressing the gene, and the color represents the average expression level.

### Ridge Plot
Displays the density of gene expression levels for each cluster. Useful for visualizing gene expression distributions within clusters.

## Using the Visualization Tools

### Gene Selection
Use the dropdown menu to select one or more genes of interest to visualize.

![](../_static/images/multiple_datasets_analysis/genes_selection_merge.png)

### Plot Generation
1. **Choose the Appropriate Plot Type**:
   Select the desired plot type (Feature Plot, Violin Plot, Dot Plot, or Ridge Plot) based on the analysis goals.
2. **Customize Plot Settings**:
   - Adjust settings such as text size, axes visibility, and color scale
   - For Feature Plot, select the minimum and maximum cutoff values
   - Refine expression levels displayed
3. **Generate and Analyze the Plot**:
   - Click the appropriate button ("Run Feature Plot", "Run Vln Plot", etc.)
   - Analyze the gene expression patterns across clusters

![](../_static/images/multiple_datasets_analysis/genes_expressions_merge.png)

## Exporting Results
Use the provided download buttons to export the generated plots in PNG format for further analysis or presentation.

> **Tip:**
> Use the Feature Plot to visualize spatial gene expression patterns and identify co-expressed genes within the same cluster.

## Additional Analysis

### Gene Expression Summary
- Input the genes you want to analyze and set an expression threshold
- Click "Analyze Expression" to summarize the number and percentage of cells expressing the selected genes
- Download the summary table in CSV format for further analysis