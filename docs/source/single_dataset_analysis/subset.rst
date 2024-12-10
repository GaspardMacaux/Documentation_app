===============================
Subset
===============================

### Overview
Subsetting allows you to create focused datasets by selecting specific cells or genes of interest. This function helps reduce dataset size and focus analysis on relevant biological questions.

### Subsetting Methods

#### 1. Cluster-Based Subsetting
- **Selection Options**:
 * Choose specific clusters
 * Multiple cluster selection
 * Select all/none option

- **Process**:
 * Select target clusters
 * Click "Apply cluster based subset"
 * New dataset created automatically

.. image:: ../_static/images/single_dataset_analysis/subset.png
  :width: 90%
  :align: center

#### 2. Gene Expression Subsetting
- **Gene Selection**:
 * Enter gene list (comma-separated)
 * Set expression threshold
 * Define minimum expressed genes

- **Parameters**:
 * Expression threshold (default: 0.1)
 * Number of genes required
 * Include/exclude options

### Visualization Options

#### Before Subsetting
- **Global UMAP**:
 * Shows complete dataset
 * Highlights selected clusters
 * Original structure visible

#### After Subsetting
- **Subset UMAP**:
 * Displays selected cells only
 * Maintains original coordinates
 * Confirms selection accuracy

### Data Export

#### Save Options
- **Format**: .RDS file
- **Content**: Complete Seurat object
- **Includes**:
 * Expression data
 * Metadata
 * Dimensional reductions

.. tip::
  * Document subsetting criteria
  * Verify cell numbers
  * Check gene lists carefully
  * Save original dataset

.. warning::
  * Check gene spelling
  * Verify threshold values
  * Monitor cell numbers
  * Backup before subsetting

### Troubleshooting

Problem | Cause | Solution
--------|-------|----------
Empty subset | Wrong criteria | Check thresholds
Missing cells | Strict filters | Adjust parameters
Gene not found | Spelling errors | Verify gene names
Large file size | Many features | Consider further filtering