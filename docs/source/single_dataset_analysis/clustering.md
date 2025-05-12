# Clustering

## Overview
Clustering is a key step in single-cell RNA sequencing analysis that groups cells with similar gene expression profiles into clusters. These clusters may correspond to different cell types, states, or other biological distinctions. In this application, clustering is performed in two main steps: **finding neighbors** and **running the clustering algorithm**. Additionally, **UMAP** is used to visualize the clusters.

## Neighbors Calculation

### Finding Nearest Neighbors
The first step in clustering is calculating the **nearest neighbors** for each cell based on their gene expression similarities.
- Number of Dimensions Parameter: 
  * Uses the PCs selected in the previous step
  * Typical range: 10-30 dimensions
  * More dimensions = more biological detail but potential noise
  * Start with 10-15 for initial analysis

### Purpose and Benefits
- Why Calculate Neighbors?
  * Foundation for clustering analysis
  * Identifies cells with similar expression profiles
  * Required for UMAP visualization
  * Creates network of cell relationships

## Running the Clustering

### Resolution Settings
After neighbor calculation, cells are grouped into clusters based on their similarities.
- Resolution Parameter (0.1-2.0):
  * Controls cluster granularity
  * Lower values (0.2-0.4): Fewer, broader clusters
  * Medium values (0.4-0.8): Balanced clustering
  * Higher values (0.8-1.2): More detailed clusters
  * Start with 0.5 and adjust based on results

### Algorithm Options
1. Original Louvain: 
   * Fast and robust
   * Good for most analyses
   * Default choice for standard datasets
2. Louvain with Multilevel Refinement:
   * More precise cluster boundaries
   * Better for complex datasets
   * Use when you need more detailed clusters
3. SLM Algorithm:
   * Optimized for finding small populations
   * Good for rare cell types
   * Use when expecting many distinct populations

![](../_static/images/single_dataset_analysis/neighbors.png)

## UMAP Visualization

### Display Options
UMAP provides a 2D representation of the clustering results.
- Visualization Options:
  * Remove Axes: Cleaner visualization
  * Remove Legend: Better for publication figures
  * Image Resolution: Adjustable for exports

### Interpretation Guide
- Interpretation:
  * Closer points = more similar cells
  * Distance between clusters suggests relationship
  * Shape and density can indicate population structure

![](../_static/images/single_dataset_analysis/clustering.png)

> **Tip:**
> * Start with default parameters (10-15 PCs, resolution 0.5)
> * Adjust resolution to split/merge clusters
> * Choose algorithm based on dataset complexity
> * Use UMAP to validate clustering quality

> **Warning:**
> * Very high resolutions can create artificial clusters
> * Too few dimensions might miss biological variation
> * Check biological markers to validate clusters
> * Document parameters for reproducibility

## Troubleshooting Guide

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| Overclustering | Resolution too high | Lower resolution parameter |
| Merged populations | Resolution too low | Increase resolution |
| Poor separation | Too few dimensions | Increase number of PCs |
| Artificial clusters | Too many dimensions/high resolution | Reduce parameters |
| No rare populations | Algorithm not sensitive enough | Try SLM algorithm |