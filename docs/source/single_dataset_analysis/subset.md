# Subset

## Overview
This section allows you to create focused datasets by selecting specific cell populations or cells with particular gene expression patterns. Subsetting helps you concentrate your analysis on specific cell types of interest while maintaining all the analysis history and annotations from the full dataset.

## What You'll Do on This Tab
- **Extract specific clusters** to focus on particular cell types
- **Filter cells by gene expression** to find cells with specific molecular signatures
- **Create smaller datasets** for detailed analysis or sharing
- **Compare original vs subset** to verify your selection
- **Export focused datasets** for specialized downstream analyses

## Why Create Subsets?
- **Focus analysis** on specific cell populations of interest
- **Reduce computational burden** for intensive analyses
- **Share specific cell types** with collaborators
- **Perform specialized analysis** (e.g., trajectory analysis on stem cells only)
- **Create publication datasets** with only relevant cell types

## Subsetting Methods Available

### Method 1: Subset by Clusters
**When to use**: You want to keep only specific cell types/clusters

**How to set up**:
1. **View the original dataset** in the UMAP plot showing all clusters
2. **Select clusters to keep** using the "Select clusters" dropdown
   - Multiple clusters can be selected
   - Only selected clusters will be retained
3. **Click "Create Subset"** to generate the new dataset

**What you get**: A new dataset containing only cells from your selected clusters

**Example use cases**:
- Extract only immune cells (clusters 2, 5, 8) for immune analysis
- Focus on stem cells and early progenitors for trajectory analysis
- Remove contaminating cell types from your dataset

### Method 2: Subset by Gene Expression
**When to use**: You want cells expressing specific combinations of genes

**How to set up**:
1. **Enter gene names** separated by commas (e.g., "Pax7, Myod1, Myog")
2. **Set expression threshold**: Minimum expression level to count as "expressing"
   - Higher values = more stringent selection
   - Lower values = include cells with low expression
3. **Set minimum expressed genes**: How many genes from your list must be expressed
   - Example: List 3 genes, require 2 = cells must express at least 2 of the 3 genes
4. **Click "Apply Gene Subsetting"** to create filtered dataset

**What you get**: Cells that meet your gene expression criteria

**Example use cases**:
- Find cells expressing both stem cell and activation markers
- Identify cells in specific pathway states
- Select cells with particular transcriptional signatures

![](../_static/images/single_dataset_analysis/subset_single.tiff)

## Analysis Pipeline

### Step 1: Examine Your Original Dataset
- **Review the global UMAP** showing all clusters and cell types
- **Identify populations of interest** based on your research question
- **Consider your subsetting strategy** - clusters vs gene expression vs combination

### Step 2: Choose Your Subsetting Method

**For Well-Defined Cell Types**:
- Use cluster-based subsetting if your clusters represent clear biological populations
- Select multiple related clusters if needed (e.g., different stages of same lineage)

**For Functional States**:
- Use gene expression subsetting to find cells in specific states
- Combine multiple genes to define complex phenotypes
- Use pathway markers or functional gene combinations

**For Complex Selections**:
- Can combine both methods sequentially
- First subset by clusters, then by gene expression within those clusters

### Step 3: Configure Your Selection

**Cluster Selection Tips**:
- Include all relevant biological populations
- Consider including transitional states if studying development
- Verify cluster annotations before subsetting

**Gene Expression Tips**:
- Start with well-characterized marker genes
- Use moderate expression thresholds initially
- Consider co-expression requirements carefully

### Step 4: Generate and Validate Subset

**Create the Subset**:
- Click appropriate button to generate subset
- System shows number of cells retained
- New UMAP plot displays only subset cells

**Validation Steps**:
- **Compare original vs subset plots** to verify correct selection
- **Check cell numbers** - ensure sufficient cells for downstream analysis
- **Verify expected populations** are present in subset

### Step 5: Export and Use Subset

**Save Your Subset**:
- Click "Save subset as .RDS" to export
- File can be loaded in new analysis sessions
- Share with collaborators or use for specialized analysis

**Quality Checks**:
- Ensure major cell types of interest are represented
- Verify no unexpected cell types were included
- Check that subset makes biological sense

## Visualization and Comparison

### Original Dataset View
- Shows complete UMAP with all clusters
- Helps identify which populations to extract
- Reference for comparing subset results

### Subset Preview
- Displays only selected cells on UMAP
- Maintains original coordinates for easy comparison
- Shows final cell composition after filtering

**How to interpret**:
- **Maintained structure** = good subset preserving biological relationships
- **Fragmented patterns** = may have over-filtered or selected unrelated populations
- **Expected cell types present** = successful subset creation

```{tip}
Always validate your subset by examining the resulting UMAP and checking that expected cell populations are present with reasonable cell numbers. A good subset should maintain biological coherence.
```

## Practical Applications

### Research-Focused Subsets
**Developmental Studies**: Extract stem cells and their progeny for trajectory analysis
**Disease Research**: Focus on affected cell types while removing healthy controls
**Cell Type Characterization**: Isolate specific populations for detailed gene expression profiling

### Technical Subsets
**Computational Efficiency**: Reduce dataset size for memory-intensive analyses
**Quality Control**: Remove low-quality or contaminating cell types
**Data Sharing**: Create clean datasets with only relevant populations

### Publication Subsets
**Figure Generation**: Focus plots on relevant cell types for clarity
**Supplementary Data**: Provide subsets corresponding to specific analyses
**Reproducibility**: Share exact cell populations used in key findings

```{warning}
Subsetting is irreversible within this analysis session. Make sure you're satisfied with your selection before proceeding. Always save both original and subset datasets for future reference.
```

## Best Practices

### Planning Your Subset
- **Define your research question** clearly before subsetting
- **Consider downstream analyses** that will be performed
- **Balance specificity with sufficient cell numbers** for statistical power

### Validation Strategy
- **Check known marker expression** in your subset
- **Verify cell type proportions** make biological sense
- **Ensure no major populations** were accidentally excluded

### Documentation
- **Record subsetting parameters** used
- **Document biological rationale** for selections
- **Note final cell numbers** and population composition

## Troubleshooting

**Too few cells in subset?**
- Relax gene expression thresholds
- Include additional related clusters
- Check if filtering criteria are too stringent

**Unexpected cell types in subset?**
- Review cluster annotations and marker gene expression
- Consider additional quality control filters
- May need to refine cluster definitions first

**Subset doesn't maintain structure?**
- May indicate over-filtering or selection of unrelated populations
- Consider including transitional cell types
- Verify biological coherence of selected populations

## Next