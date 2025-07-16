# Heat Maps & Dual Expression

## Overview
This section provides advanced visualization tools to explore relationships between multiple genes and examine correlations between gene pairs. Heatmaps show expression patterns across many genes simultaneously, while dual expression analysis reveals how two genes relate to each other at the single-cell level.

## Heatmap Analysis

### When to use Heatmaps
- Compare expression of many genes across all clusters at once
- Identify gene expression signatures for each cluster
- See which genes are co-expressed or oppositely expressed
- Create publication-ready figures showing cluster characterization

### Gene Selection Options

**Manual Gene Selection**
- Use the gene picker to select specific genes of interest
- Best when you have candidate markers or genes of interest
- Allows precise control over which genes to display

**Automatic Top Genes**
- Check "Use top 10 genes per cluster" for automated selection
- System finds the most differentially expressed genes for each cluster
- Good for exploratory analysis when you don't know which genes to examine
- Ensures each cluster has representative markers

### Cluster Selection

**All Clusters**
- Select "Select All Clusters" to include every cluster
- Good for comprehensive overview
- May be crowded if you have many clusters

**Specific Clusters**
- Enter cluster numbers separated by commas (e.g., "0,1,3,5")
- Focus on clusters of particular interest
- Reduces complexity for cleaner visualization

### How to Read the Heatmap
- **Rows** = genes, **Columns** = clusters
- **Color intensity**: Darker colors = higher expression
- **Color scale**: Usually red = high expression, blue = low expression
- **Patterns**: Look for genes that are high in some clusters, low in others

![](../_static/images/single_dataset_analysis/heatmap_single.tiff)

## Dual Expression Analysis

### When to use Dual Expression
- Check if two genes are co-expressed in the same cells
- Identify cells expressing both markers simultaneously
- Examine relationships between transcription factors and target genes
- Validate co-expression patterns suggested by other analyses

### How to Set Up
**Gene Selection**
- **First Gene**: Select your primary gene of interest
- **Second Gene**: Choose the gene you want to compare against
- Can examine any two genes from your dataset

**Cluster Focus**
- **All Clusters**: Include all cells in the analysis
- **Specific Clusters**: Enter cluster numbers to focus on particular cell types
- Useful for examining co-expression within specific populations

### How to Read the Dual Expression Plot
- **X-axis** = expression of first gene
- **Y-axis** = expression of second gene  
- **Each dot** = one individual cell
- **Dot position** shows both genes' expression in that cell

**Expression Patterns:**
- **Bottom-left corner**: Cells expressing neither gene
- **Top-right corner**: Cells expressing both genes highly
- **Diagonal pattern**: Genes are co-expressed (correlated)
- **Scattered pattern**: Genes are independently expressed
- **Corner clusters**: One gene high, other low (mutually exclusive)

![](../_static/images/single_dataset_analysis/dualexpression_single.tiff)

## Analysis Pipeline

### Step 1: Choose Your Analysis Type
- **Heatmap**: For systematic multi-gene comparison
- **Dual Expression**: For specific two-gene relationships

### Step 2: Configure Gene Selection
**For Heatmap:**
- Select specific genes OR use automatic top genes
- Consider 10-50 genes for readable visualization

**For Dual Expression:**
- Pick two genes with biological relevance
- Consider transcription factors, pathway components, or co-markers

### Step 3: Set Cluster Parameters
- Include all clusters for comprehensive view
- Focus on specific clusters for detailed analysis
- Consider your biological question

### Step 4: Generate and Interpret
- Click "Generate Heatmap" or "Generate Dual Expression"
- Examine patterns for biological insights
- Export high-quality images for presentations

### Step 5: Export Results
- Choose appropriate resolution (300 DPI for publications)
- Select format based on use (TIFF for publications, PNG for presentations)
- Download plots for further analysis

```{tip}
For heatmaps, start with automatic top genes to get an overview, then create focused heatmaps with specific genes of interest. For dual expression, examine known co-expressed gene pairs first to validate your data.
```

## Practical Applications

**Heatmap Use Cases:**
- Characterize each cluster with its top marker genes
- Compare related gene families across clusters
- Identify co-regulated gene modules
- Create figures for publications showing cluster identity

**Dual Expression Use Cases:**
- Check co-expression of transcription factor and target genes
- Examine stem cell markers vs differentiation markers
- Validate pathway activation (receptor + downstream genes)
- Identify rare cell populations expressing multiple markers

```{warning}
Large heatmaps with many genes can be difficult to read. Consider using 10-30 genes maximum for clear visualization. For dual expression, make sure both genes are actually expressed in your dataset.
```

## Troubleshooting

**Heatmap too crowded?**
- Reduce number of genes or clusters
- Use hierarchical clustering to group similar genes
- Focus on top differentially expressed genes

**No clear patterns in heatmap?**
- May need better cluster resolution
- Consider using more stringent gene selection
- Check if normalization was performed correctly

**Dual expression shows no correlation?**
- Genes may be expressed in different cell types
- Try focusing on specific clusters where both genes are active
- Consider examining related pathway components