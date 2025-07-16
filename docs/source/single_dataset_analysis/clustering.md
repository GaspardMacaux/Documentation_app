# Clustering

## Overview
Clustering groups cells with similar gene expression patterns to identify distinct cell populations. This step uses the principal components from the previous analysis to find neighborhoods of similar cells, then groups them into clusters that may represent different cell types or states.

## What is Neighbor Calculation, Clustering, and UMAP?

**Neighbor Calculation**
- Identifies cells with similar gene expression profiles in the reduced PC space
- Creates a network where each cell is connected to its most similar neighbors
- Forms the foundation for both clustering and visualization

**Clustering**
- Groups connected cells into distinct clusters based on their neighborhood relationships
- Uses community detection algorithms to find densely connected cell groups
- Each cluster potentially represents a different cell type or biological state

**UMAP (Uniform Manifold Approximation and Projection)**
- Creates a 2D visualization of the high-dimensional data
- Preserves both local neighborhoods and global structure
- Allows visual inspection of cluster separation and relationships

## Analysis Pipeline

### Step 1: Find Cell Neighbors

![](../_static/images/single_dataset_analysis/cluster_tab_single.tiff)

**Number of Dimensions**
- Select how many principal components to use (default: 10)
- More dimensions = capture more biological detail but include more noise
- Use the elbow plot from previous step to guide this choice
- Typical range: 10-30 dimensions

**Find Neighbors**
- Click "Find neighbors" to calculate cell-to-cell similarities
- Creates a shared nearest neighbor graph
- Also automatically runs UMAP for visualization

![](../_static/images/single_dataset_analysis/voisin_single.tiff)

### Step 2: Identify Clusters

**Resolution Parameter**
- Controls how finely cells are grouped (default: 0.5)
- **Lower values (0.1-0.3)**: Fewer, broader clusters
- **Medium values (0.4-0.8)**: Balanced clustering  
- **Higher values (0.8-2.0)**: More detailed, smaller clusters
- Start with 0.5 and adjust based on biological expectations

**Clustering Algorithm**
- **Original Louvain**: Fast and reliable, good for most analyses
- **Louvain with Multilevel Refinement**: More thorough, better for complex datasets
- **SLM Algorithm**: Optimized for very large datasets, fastest option

**Find Clusters**
- Click "Find clusters" to group cells based on the neighbor graph
- Results show clusters colored on the UMAP plot

![](../_static/images/single_dataset_analysis/cluster_single.tiff)

### Step 3: Export Results

**File Format Selection**
- Choose export format: TIFF, PNG, PDF, JPEG, or SVG
- TIFF recommended for publications (lossless, high quality)
- PNG good for presentations and web use

**Resolution (DPI)**
- Set image resolution for downloads (default: 300)
- 300 DPI: Standard quality for most uses
- 600+ DPI: High quality for publications

**Display Options**
- Remove Axes: Cleaner plots without axis lines and numbers
- Remove Legend: Minimal plots without cluster color legend

**Download UMAP**
- Click to save the clustering visualization
- Includes all current display settings and colors

```{tip}
Start with default settings (10-15 dimensions, resolution 0.5, Original Louvain) then adjust based on your results. Higher resolution creates more clusters - increase if you expect many cell types.
```

## Expected Results

After completing this pipeline:
- Cells are grouped into distinct clusters visible on UMAP
- Each cluster potentially represents a different cell type or state
- Cluster numbers are assigned automatically
- Ready for biological interpretation and marker gene analysis

## Optimization Guidelines

**Too Few Clusters?**
- Increase resolution parameter
- Try Louvain with Multilevel Refinement
- Check if enough dimensions were used

**Too Many Clusters?**
- Decrease resolution parameter
- May indicate overclustering of the same cell type
- Consider if biological heterogeneity is expected

**Poor Cluster Separation?**
- May need more dimensions from PCA
- Check data quality and batch effects
- Consider different clustering algorithm

```{warning}
The resolution parameter significantly affects downstream analysis. Biological validation with known markers is essential to confirm clusters represent true cell types rather than technical artifacts.
```

## Choosing the Right Parameters

**Dimensions**: Use elbow plot guidance, typically 10-30
**Resolution**: Start at 0.5, adjust in 0.1 increments based on results
**Algorithm**: Original Louvain for most cases, SLM for speed with large datasets

## Next Steps

Once satisfied with clustering:
- Examine cluster-specific gene expression
- Identify marker genes for each cluster
- Assign biological identities based on known markers
- Consider whether clusters need merging or splitting