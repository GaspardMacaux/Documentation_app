# Data Cleanup & Variable Features

## Overview
This section performs quality control and data preprocessing - essential steps before any analysis. Poor quality cells and technical artifacts are removed, and the data is normalized to make cells comparable.

## Analysis Pipeline

### Step 1: Visualize Data Quality

**QC Metrics Plot**
- Click "QC metrics plot" to display violin plots showing:
  - Number of genes per cell (nFeature_RNA)
  - Number of UMI counts per cell (nCount_RNA) 
  - Percentage of mitochondrial genes (percent.mt)
- These plots help you identify outlier cells and set appropriate filtering thresholds

![](../_static/images/single_dataset_analysis/qc_single.tiff)

**Feature Scatter Plots**
- Click "Feature Scatter Plots" to see relationships between metrics:
  - UMI count vs mitochondrial percentage
  - UMI count vs number of genes
- Helps identify cells with unusual patterns (e.g., high mitochondrial content)

### Step 2: Set Quality Control Thresholds

**Unique Genes Detected Slider**
- Sets the acceptable range of genes per cell (default: 200-2500)
- Cells with too few genes may be empty droplets or dying cells
- Cells with too many genes might be doublets (two cells captured together)

**Maximum Mitochondrial % Slider**  
- Sets maximum allowed mitochondrial gene percentage (default: 5%)
- High mitochondrial content often indicates cell stress or death
- Should be lower for single-nucleus data (~2%) vs single-cell data (~5-10%)

**Scale Factor**
- Normalization factor applied to all cells (default: 10,000)
- Standardizes library sizes across cells before log-transformation

### Step 3: Apply Quality Filters

**Apply QC Filters**
- Click this button to remove cells that don't meet your criteria
- The system will show how many cells were retained vs filtered out
- This step cannot be undone, so ensure your thresholds are appropriate

```{warning}
Once you apply QC filters, filtered cells are permanently removed from the analysis. Check your thresholds carefully using the plots first.
```

### Step 4: Identify Variable Features

**Number of Variable Features**
- Enter the number of highly variable genes to identify (default: 2000)
- These genes show high cell-to-cell variation and drive downstream analysis
- More features = more biological detail but potentially more noise

**Normalize Data**
- Click to perform log-normalization and identify variable features
- This standardizes expression values and selects genes for clustering
- A plot will show the most variable genes with labels

![](../_static/images/single_dataset_analysis/normalise_single.tiff)

```{tip}
Start with default parameters (200-2500 genes, 5% mitochondrial, 2000 variable features) and adjust based on your specific dataset and experimental conditions.
```

## Expected Results

After completing this pipeline:
- Low-quality cells are removed
- Expression data is normalized across cells  
- Top variable genes are identified for downstream analysis
- You can proceed to dimensional reduction and clustering

## Key Quality Metrics

- **Cells retained**: Aim to keep 80-95% of cells after filtering
- **Genes per cell**: Should follow expected distribution for your cell type
- **Mitochondrial content**: Should be low and consistent across cells
- **Variable features**: Should include known marker genes for your system

## Troubleshooting

**Too few cells retained?**
- Relax filtering thresholds
- Check if your data has unusual characteristics

**Unusual distributions?**
- May indicate batch effects or experimental issues
- Consider more stringent filtering

**No clear variable features?**  
- May need more cells or deeper sequencing
- Check data quality and preprocessing