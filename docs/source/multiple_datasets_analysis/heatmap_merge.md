# Heatmaps and Dual Expression Analysis

## Overview
This section provides two powerful visualization tools for analyzing gene expression patterns across your datasets:
1. Heatmaps: Visualize expression patterns of multiple genes simultaneously
2. Dual Expression Analysis: Compare expression levels between pairs of genes

## Heatmap Visualization

### What is a Heatmap?
- Matrix-like visualization where rows represent genes and columns represent clusters/datasets
- Color intensity indicates expression level
- Helps identify patterns across multiple genes simultaneously

### Creating Your Heatmap

#### Step 1: Gene Selection
- Use the "Select Genes" dropdown menu to choose genes
- Options:
  * Manual selection: Pick specific genes of interest
  * Automatic selection: Check "Use top 10 genes per cluster"
  * Search functionality available for finding specific genes

#### Step 2: Group Selection
- Choose how to group your data:
  * By dataset: Compare between different samples/conditions
  * By cluster: Compare between cell types
- Specify clusters:
  * Enter specific clusters in comma-separated format
  * Or select "Select All Clusters" for complete analysis

#### Step 3: Generate and Customize
- Click "Generate Heatmap" to create visualization
- Adjust resolution for download (default: 300 DPI)
- Download the heatmap for presentations or publication

### Tips for Heatmap Analysis
- Start with a small set of known marker genes
- Add genes gradually to maintain clarity
- Consider using cluster-specific top genes
- Group similar clusters together for better pattern visualization

## Dual Expression Analysis

### What is Dual Expression?
- Scatter plot comparing expression levels of two genes
- Each point represents a cell
- Reveals relationships between gene pairs
- Helps identify co-expression patterns

### Creating Dual Expression Plots

#### Step 1: Gene Selection
- Choose two genes to compare:
  * First gene selector: Primary gene of interest
  * Second gene selector: Gene to compare against
- Use search functionality to find specific genes

#### Step 2: Configure Display
- Select grouping method:
  * Dataset: Color points by sample origin
  * Cluster: Color points by cell type
- Choose clusters to include:
  * Enter specific clusters or
  * Select all clusters for complete comparison

#### Step 3: Generate and Export
- Click "Generate Dual Expression" to create plot
- Adjust resolution as needed
- Download for further use