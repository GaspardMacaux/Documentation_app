# Dimensional Reduction

## Overview
This step reduces data complexity while preserving biological signals. Single-cell data typically contains thousands of genes per cell - too many dimensions for effective analysis. We use scaling and Principal Component Analysis (PCA) to identify the main sources of variation and focus on the most informative components.

## What is Data Scaling and PCA?

**Data Scaling**
- Normalizes each gene's expression to give equal weight to all genes
- Prevents highly-expressed genes from dominating the analysis
- Centers gene expression to mean 0 and scales to unit variance

**Principal Component Analysis (PCA)**
- Identifies the main sources of variation in your data
- Transforms thousands of gene measurements into a smaller set of meaningful components
- Each component captures a different aspect of biological variation
- Reduces noise while preserving important biological signals

## Analysis Pipeline

### Step 1: Scale Data and Calculate PCA

**Scale Data & Run PCA**
- Click "Scale Data & Run PCA" to perform both operations
- Scaling standardizes all genes to comparable ranges
- PCA calculates principal components from the variable features identified earlier
- Results show PCA table with top contributing genes and loading plots

![](../_static/images/single_dataset_analysis/pca_single.tiff)

### Step 2: Determine Optimal Number of Components

**Show Elbow Plot**
- Click "Show Elbow Plot" to visualize how much variance each component explains
- The plot shows percentage of variance on Y-axis vs principal components on X-axis
- Look for the "elbow" - the point where adding more components gives diminishing returns

![](../_static/images/single_dataset_analysis/elbow_single.tiff)

**How to Read the Elbow Plot:**
- Sharp drop initially = first components capture major variation
- Gradual decline = later components add less information
- "Elbow point" = optimal balance between detail and noise
- Typically use 10-30 components for downstream analysis

```{tip}
Look for the point where the curve starts to flatten - this "elbow" indicates the optimal number of dimensions to use for clustering. Usually between 10-30 components.
```

## Expected Results

After completing this pipeline:
- Data is scaled and ready for clustering
- Principal components are calculated and ranked by importance
- You have identified the optimal number of dimensions for downstream analysis
- Ready to proceed to clustering with appropriate PC selection

## Choosing the Right Number of PCs

**Guidelines:**
- **Too few PCs**: May miss important biological variation
- **Too many PCs**: Include technical noise and random variation
- **Typical range**: 15-30 PCs for most datasets
- **Consider**: Dataset complexity, number of cell types expected

```{warning}
The number of principal components you choose will affect all subsequent analyses including clustering and UMAP visualization. Take time to examine the elbow plot carefully.
```

## Troubleshooting

**No clear elbow?**
- May indicate batch effects or low data quality
- Consider more stringent quality control
- Check if enough variable features were selected

**Very steep decline?**
- May suggest strong batch effects or dominant cell populations
- Consider using more PCs to capture subtle populations

**Flat curve throughout?**
- May indicate insufficient biological variation
- Check data quality and cell diversity