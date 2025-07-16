# Heatmaps & Dual Expression - Multiple Datasets

## Overview
This section provides advanced visualization tools for comparing gene expression patterns across multiple datasets. You can create comprehensive heatmaps showing expression across datasets and clusters, and examine correlations between gene pairs using dual expression scatter plots.

## What You'll Do on This Tab
- **Generate heatmaps** comparing gene expression across datasets and clusters
- **Create dual expression plots** to examine gene correlations between datasets
- **Compare expression patterns** systematically across experimental conditions
- **Export high-quality visualizations** for publications and presentations

## Heatmap Analysis

### Gene Selection for Heatmaps

**Manual Gene Selection**:
- Use the gene picker to select specific genes of interest
- Best when you have known markers or candidate genes
- Allows precise control over which genes to display

**Automatic Top Genes**:
- Check "Use top 10 genes per cluster" for automated selection
- System finds most differentially expressed genes for each cluster
- Good for exploratory analysis across all datasets
- Ensures representative markers from each cell population

### Grouping and Clustering Options

**Group By Selection**:
- **Dataset**: Compare expression between different experimental conditions
- **Cluster**: Compare expression between cell types across all datasets

**Assay Selection**:
- **RNA**: Original expression data preserving dataset-specific patterns
- **Integrated**: Batch-corrected data for normalized comparisons

**Cluster Selection**:
- **Select All Clusters**: Include every cluster for comprehensive view
- **Specify Clusters**: Enter cluster numbers (comma-separated) to focus on specific populations

### How to Read Heatmaps

**Heatmap Structure**:
- **Rows**: Genes selected for analysis
- **Columns**: Datasets or clusters (depending on Group By setting)
- **Color intensity**: Expression level (usually red = high, blue = low)

**Pattern Recognition**:
- **Consistent columns**: Genes with similar expression across conditions
- **Dataset-specific patterns**: Genes showing condition-specific expression
- **Cluster-specific patterns**: Cell type markers conserved across datasets

![](../_static/images/multiple_datasets_analysis/heatmap_merge.png)

## Dual Expression Analysis

### When to Use Dual Expression
- **Compare gene correlations** between datasets
- **Validate co-expression** across experimental conditions
- **Identify condition-specific** gene relationships
- **Examine pathway coordination** between different datasets

### Setup Configuration

**Gene Selection**:
- **First Gene**: Select primary gene of interest
- **Second Gene**: Choose gene to correlate with the first
- Can examine any two genes present in your datasets

**Grouping Options**:
- **Dataset**: Color points by dataset origin to compare correlations
- **Cluster**: Color points by cell type to see population-specific patterns

**Cluster Filtering**:
- **Select All Clusters**: Include all cell populations
- **Specify Clusters**: Focus on particular cell types of interest

### How to Read Dual Expression Plots

**Plot Structure**:
- **X-axis**: Expression of first selected gene
- **Y-axis**: Expression of second selected gene
- **Each point**: One individual cell
- **Point color**: Dataset or cluster identity (based on grouping choice)

**Correlation Patterns**:
- **Diagonal trend**: Genes are positively correlated
- **Scattered pattern**: Genes are independently expressed
- **Inverse diagonal**: Genes are negatively correlated
- **Distinct clusters**: Different cell populations or datasets show different correlation patterns

**Dataset Comparison**:
- **Overlapping patterns**: Similar gene relationships across datasets
- **Separated patterns**: Dataset-specific gene correlations
- **Shifted distributions**: Expression level differences between conditions

## Analysis Pipeline

### Step 1: Choose Analysis Type
- **Heatmap**: For systematic multi-gene comparison across datasets/clusters
- **Dual Expression**: For specific two-gene relationship analysis

### Step 2: Configure Gene Selection
**For Heatmaps**:
- Select 10-50 genes for optimal visualization
- Use automatic selection for exploratory analysis
- Use manual selection for hypothesis testing

**For Dual Expression**:
- Choose biologically relevant gene pairs
- Consider pathway components, co-regulators, or competing factors

### Step 3: Set Grouping Parameters
- **Dataset grouping**: Compare conditions or treatments
- **Cluster grouping**: Compare cell types
- **Combined analysis**: Use both for complex comparisons

### Step 4: Generate and Interpret
- Create visualizations using configured parameters
- Look for patterns that validate or challenge biological expectations
- Note differences between datasets or clusters

### Step 5: Export Results
- Download high-quality images for presentations
- Adjust resolution based on intended use
- Save analysis parameters for reproducibility
`

## Export and Customization

### Heatmap Export Options
- **Format selection**: PNG, PDF, TIFF, JPEG
- **Resolution control**: Adjust DPI for publication quality (default: 300)

```{warning}
Large heatmaps with many genes and conditions can be difficult to interpret. Consider focusing on specific gene sets or using hierarchical clustering to organize related genes together.
```

## Troubleshooting

**Heatmap appears empty or uniform?**
- Check if selected genes are expressed in your data
- Verify grouping produces meaningful comparisons
- Consider using different assay (RNA vs Integrated)

**Dual expression shows no correlation?**
- Genes may be expressed in different cell types
- Try focusing on specific clusters where both genes are active
- Check if genes are actually co-expressed in your system

**Patterns don't match expectations?**
- Validate with known biology and literature
- Check for batch effects between datasets
- Consider if integration parameters need adjustment

**Visualization quality issues?**
- Increase resolution for better quality
- Adjust plot dimensions for optimal gene label readability
- Consider reducing number of genes or conditions for clarity