# Clustering Multiple Datasets

## Overview
After loading and integrating your datasets, the clustering step helps identify distinct cell populations based on gene expression patterns. This process involves several key steps: data scaling, dimensional reduction, optional batch effect correction with Harmony, and finally, cell clustering.

## Step-by-Step Process

### Scaling and Dimensional Reduction
First, click "Run Scaling, PCA and Elbow Plot". This performs three essential operations:
- Scales your data to make genes comparable
- Calculates Principal Component Analysis (PCA)
- Generates an Elbow Plot to help determine optimal dimensions

![](../_static/images/multiple_datasets_analysis/scaling_PCA_merge.png)

### Optional: Harmony Integration
If your datasets show batch effects, you can use Harmony integration:
- Click "Run Harmony Integration"
- In Harmony Settings:
  * Select variables to integrate (like "dataset" or "condition")
  * Set number of dimensions (default: 15)

## Clustering Setup

### Number of Dimensions
- Default value: 15
- Range: 1 to maximum PCs available
- How to choose: Look at the Elbow Plot where variance explained plateaus
- Impact: Higher values include more information but increase noise

![](../_static/images/multiple_datasets_analysis/neighbors_merge.png)

### Resolution for Clustering
- Default value: 0.5
- Range: 0.01 to 2.0
- How to adjust:
  * Lower values (0.1-0.3): Fewer, broader clusters
  * Medium values (0.4-0.8): Balanced clustering
  * Higher values (>0.8): More detailed, smaller clusters
- Impact: Determines how finely the cells are grouped

### Clustering Algorithm Options
1. **Original Louvain**
   - Best for: General purpose clustering
   - Characteristics: Fast, reliable
   - Good starting point for most analyses

2. **Louvain with Multilevel Refinement**
   - Best for: Large datasets
   - Characteristics: More thorough, slower
   - Can find more subtle clusters

3. **SLM Algorithm**
   - Best for: Very large datasets
   - Characteristics: Fastest option
   - May miss some subtle clusters

![](../_static/images/multiple_datasets_analysis/clustering_merge.png)

## Visualization Options

### UMAP Plot Customization
- Remove Axes: Hides axis lines and labels
- Remove Legend: Hides cluster labels
- DPI for UMAP Download: Adjust image resolution
  * 300 DPI: Standard quality
  * 600 DPI: High quality
  * 1200 DPI: Publication quality

## Workflow Order

### Initial Analysis
1. Run Scaling, PCA and view Elbow Plot
2. Decide if Harmony integration is needed
3. Run Harmony if required

### Clustering Steps
1. Set dimensions based on Elbow Plot
2. Start with default resolution (0.5)
3. Choose Original Louvain algorithm
4. Click "Find Neighbors and run UMAP"
5. Click "Find clusters"

## Optimization Guide
- If clusters look too broad: Increase resolution
- If clusters look too fragmented: Decrease resolution
- If clustering is slow: Try SLM algorithm
- If subtle populations are important: Try Louvain with Multilevel Refinement

## Best Practices

### Resolution Adjustment
- Start at 0.5
- Increase in 0.1 increments if you need more clusters
- Decrease if you see too many clusters
- Consider your biological expectations

### Dimension Selection
- Look for the "elbow" in the Elbow Plot
- Usually between 10-30 dimensions
- Too few: Miss important variation
- Too many: Include noise

### Algorithm Selection
- Start with Original Louvain
- Switch to SLM if speed is an issue
- Use Multilevel Refinement for detailed analysis

## References
1. Korsunsky, I., Millard, N., Fan, J. et al. Fast, sensitive and accurate integration of single-cell data with Harmony. Nat Methods 16, 1289–1296 (2019). https://doi.org/10.1038/s41592-019-0619-0