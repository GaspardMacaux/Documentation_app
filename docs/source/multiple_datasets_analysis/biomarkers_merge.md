# Cluster Biomarkers

## Overview
Identifying cluster-specific biomarkers is essential for distinguishing between different cell types or states within integrated datasets. Biomarkers are genes that are uniquely or highly expressed in a particular cluster, serving as molecular signatures for those clusters.

## Understanding Biomarkers
Biomarkers are characteristic genes whose expression levels are indicative of specific biological states or cell types. In the context of clustering, biomarkers help:
- Differentiate between clusters by their unique gene expression profiles
- Understand the functional properties of different cell populations
- Identify potential targets for therapeutic intervention or further study

## Biomarker Analysis Process

### Biomarker Discovery
Use differential expression analysis to find genes that are significantly upregulated in a cluster compared to others. This can be done through the interface by selecting clusters and applying the analysis tools.

### Comparison Tools
1. **Compare One Cluster with All Others**
   - Select a cluster to find biomarkers
   - Compare against all other clusters
   - Adjust thresholds to refine analysis
2. **Compare Two Clusters**
   - Choose two clusters for direct comparison
   - Identify differentially expressed genes
   - Analyze specific differences
3. **Cross-Dataset Cluster Comparison**
   - Select clusters from two different datasets
   - Compare gene expression profiles
   - Validate findings across conditions

### Visualization
Use visualization tools like UMAP plots to display the spatial distribution of biomarkers across clusters.

![](../_static/images/multiple_datasets_analysis/biomarkers_merge.png)

## Using the Interface

### UMAP Plot Filtering
- Visualize clusters in UMAP plot
- Filter based on specific datasets
- Download filtered plots

### Biomarker Analysis
- Select cluster for comparison
- Click "Start analysis"
- Adjust thresholds:
  * Log2 Fold Change
  * Percentage threshold
- Download gene lists

### Cluster Comparison
- Compare specific clusters
- Run cross-dataset analysis
- Download comparison results

### Cluster Table Generation
- Generate overview table
- View cluster identities
- Review biomarker information