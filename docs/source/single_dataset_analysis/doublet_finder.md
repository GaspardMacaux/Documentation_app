# Doublet Detection

## Overview
Doublet detection identifies and removes cells that are actually two cells captured together during the single-cell isolation process. These "doublets" have mixed gene expression profiles that can create artificial cell types and confound downstream analysis. DoubletFinder uses artificial doublets to train a classifier that identifies real doublets in your data.

## What are Doublets and Why Remove Them?

**What are Doublets?**
- Two or more cells captured and sequenced together as if they were a single cell
- Result in mixed gene expression signatures from multiple cell types
- Can create false intermediate cell states or artificial cell types

**Why Use DoubletFinder?**
- Prevents artificial clusters that don't represent real biology
- Improves accuracy of cell type identification
- Uses machine learning approach with artificial doublets for training
- More accurate than simple filtering based on gene/UMI counts alone

## Analysis Pipeline

### Step 1: Set Detection Parameters

**Expected Doublet Rate (%)**
- Percentage of doublets expected in your dataset
- **10x Genomics standard rates**:
  - ~0.8% per 1,000 cells loaded
  - 5,000 cells ≈ 4% doublets
  - 10,000 cells ≈ 8% doublets
- Check your protocol specifications for exact rates

**Number of PCs**
- Principal components to use for doublet detection (default: 10)
- Should match or be similar to clustering analysis
- More PCs = more sensitive but potentially more false positives

**pN Value**
- Proportion of artificial doublets to generate (default: 0.25)
- Usually kept at default unless optimization is needed
- Higher values = more training data but slower processing

**pK Value**
- Neighborhood size parameter for doublet detection (default: 0.09)
- Can be optimized automatically by the algorithm
- Affects sensitivity vs specificity balance

![](../_static/images/single_dataset_analysis/doubletfinder.png)

### Step 2: Run Doublet Detection

**Detect Doublets**
- Click "Detect Doublets" to run the DoubletFinder algorithm
- Process creates artificial doublets, trains classifier, and scores real cells
- Results show UMAP with detected doublets highlighted in red
- Statistics table shows counts and percentages

### Step 3: Review and Remove Doublets

**Review Results**
- Check UMAP visualization - doublets should be scattered or form unclear clusters
- Examine statistics table for reasonable doublet percentage
- Verify detected doublets match expected rate from your protocol

**Remove Doublets** 
- Click "Remove Doublets" to filter them from the dataset
- This permanently removes doublet cells from further analysis
- Updated cell count will be displayed

```{tip}
Expected doublet rates depend on cell loading density. For 10x Genomics: ~0.8% per 1,000 cells. So 10,000 cells should have ~8% doublets.
```

## Expected Results

After completing this pipeline:
- Doublet cells are identified and visualized on UMAP
- Statistics show the number and percentage of doublets detected
- Option to remove doublets for cleaner downstream analysis
- Remaining cells represent genuine single-cell profiles

## Parameter Optimization

**Doublet Rate Too High?**
- Check if pK value needs adjustment
- May indicate technical issues with cell isolation
- Consider if rate matches your experimental protocol

**Doublet Rate Too Low?**
- Increase expected doublet rate parameter
- Check if pN or pK values need optimization
- May indicate high-quality cell isolation

**Doublets in Unexpected Locations?**
- May indicate batch effects or poor quality data
- Check clustering quality and data preprocessing
- Consider adjusting PC number used

```{warning}
Removing doublets is irreversible in this analysis. Make sure the detected doublet rate matches your experimental expectations before removal.
```

## Validation Tips

**Good Doublet Detection:**
- Doublet rate matches expected protocol rate (±2-3%)
- Doublets are scattered across clusters, not forming coherent groups
- No obvious biological cell types are being removed

**Problematic Detection:**
- Rate much higher/lower than expected
- Doublets form coherent clusters that look biological
- Known rare cell types are being flagged as doublets

## Next Steps

After doublet removal:
- Re-examine clustering to see if artificial clusters disappeared
- Proceed with gene expression analysis on cleaned dataset
- Note the final cell count for documentation and publication