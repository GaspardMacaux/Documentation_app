===============================
Heat Maps & Dual Expression
===============================

### Overview
Heat maps and dual expression analyses are powerful tools for visualizing gene expression patterns across your dataset. Heat maps show expression levels of multiple genes across clusters, while dual expression analysis reveals relationships between pairs of genes.

### Heat Map Analysis

#### Features and Options
- **Gene Selection**:
  * Choose specific genes of interest
  * Select multiple genes simultaneously
  * Use search function for quick gene finding

- **Clustering Options**:
  * Specify clusters to include
  * Select/deselect all clusters
  * Customize cluster order

- **Visualization Settings**:
  * Adjust color scheme
  * Set resolution for export
  * Modify plot dimensions

#### Interpretation Guide
- **Color Intensity**:
  * Darker = Higher expression
  * Lighter = Lower expression
  * White = No expression

- **Clustering Patterns**:
  * Rows = Genes
  * Columns = Clusters/Cells
  * Dendrograms show relationships

### Dual Expression Analysis

#### Setup and Options
- **Gene Selection**:
  * Pick first target gene
  * Select second gene for comparison
  * Option to include specific clusters

- **Visualization Controls**:
  * Point size adjustment
  * Color scheme selection
  * Resolution settings

#### Analysis Features
- **Co-expression Patterns**:
  * X-axis = First gene
  * Y-axis = Second gene
  * Points = Individual cells

- **Pattern Interpretation**:
  * Diagonal = Correlated expression
  * Scattered = Independent expression
  * Clusters = Cell populations

.. tip::
   * Start with known marker genes
   * Use scaled data for better comparison
   * Consider biological relationships
   * Export high-resolution for publication

.. warning::
   * Avoid too many genes in heatmaps
   * Check gene name spelling
   * Consider expression ranges
   * Validate unexpected patterns

### Troubleshooting Guide

Problem | Cause | Solution
--------|-------|----------
Cluttered heatmap | Too many genes | Reduce gene selection
No visible patterns | Poor scaling | Adjust color scales
Missing data | Gene name errors | Check gene identifiers
Low resolution | Export settings | Increase DPI
Unclear relationships | Noisy data | Filter low-quality cells