# Load CellChat Analysis

## Overview
CellChat is a tool for analyzing cell-cell communication through ligand-receptor interactions in single-cell transcriptomics data. This analysis reveals how different cell types communicate with each other by identifying which cells send signals (ligands) and which cells receive them (receptors).

## What You'll Do on This Tab
- **Load your Seurat object** containing single-cell data with cell type annotations
- **Select your species** to use the appropriate ligand-receptor database
- **Load the GaspouDB database** - a comprehensive collection of ligand-receptor interactions
- **Prepare data** for cell-cell communication analysis

## Why Use CellChat?
- **Identify communication networks** between different cell types
- **Understand signaling pathways** active in your tissue
- **Discover** which cell types are "senders" vs "receivers" of signals
- **Compare communication patterns** between different conditions or treatments
- **Find potential therapeutic targets** in cell communication pathways

## GaspouDB: Our Integrated Database

### What is GaspouDB?
GaspouDB is a comprehensive ligand-receptor interaction database that combines four major resources to provide the most complete coverage of cell-cell communication interactions.

**Components of GaspouDB:**
1. **CellChatDB base interactions**: Core validated ligand-receptor pairs
2. **MultiNicheDB database**: Multi-cellular niche interactions 
3. **CellPhoneDB database**: Curated ligand-receptor interactions
4. **CellTalkDB database**: Literature-derived communication pairs

### Why Use an Integrated Database?
- **More comprehensive coverage** than any single database alone
- **Validated interactions** from multiple sources increase confidence
- **Species-specific curation** ensures accurate gene names and interactions
- **Regular updates** with latest interaction discoveries

## Analysis Pipeline

### Step 1: Load Your Seurat Object

**Data Requirements**:
- **Seurat object** saved as .rds file
- **Cell type annotations** must be present in metadata
- **Quality-controlled data** with normalized expression values
- **Sufficient cells per cell type** for reliable analysis (minimum ~20 cells recommended)

**How to load**:
1. Click "Choose File" under "Upload Seurat RDS file"
2. Select your preprocessed .rds file
3. Wait for validation and loading confirmation

**What the system checks**:
- File format is valid Seurat object
- Cell type annotations are present
- Expression data is available
- Sufficient cells for analysis

### Step 2: Configure Species Settings

**Species Selection**:
- Choose between **"Mouse"** or **"Human"**
- This determines which gene names and interactions to use
- Must match the species of your experimental data

**Why species matters**:
- Gene names differ between species (e.g., human: CD4, mouse: Cd4)
- Ligand-receptor interactions may be species-specific
- Database contains species-appropriate gene symbols

### Step 3: Load the GaspouDB Database

**Loading Process**:
1. Click "Load Database" button
2. System loads species-specific interactions from all 4 component databases
3. Prepares interaction network for your analysis
4. Validates gene names against your Seurat object

**What happens during loading**:
- Retrieves ligand-receptor pairs for your species
- Filters interactions to genes present in your dataset
- Prepares signaling pathway information
- Creates interaction probability models

### Step 4: Monitor Loading Progress

**Processing Logs**:
- Real-time status updates appear in the "Processing Logs" section
- Shows progress through each loading step
- Alerts to any issues or warnings
- Confirms successful database preparation

**Common log messages**:
- "Loading Seurat object..." = File is being processed
- "Species set to [Mouse/Human]" = Species configuration confirmed
- "Database loaded successfully" = Ready for analysis
- "X interactions found" = Number of relevant ligand-receptor pairs

![](../_static/images/cellchat_analysis/cellchat_load.png)

## Expected Results

After completing this pipeline:
- Seurat object is loaded and validated
- Species-appropriate database is prepared  
- Ligand-receptor interactions are ready for analysis
- System shows number of cells, cell types, and available interactions
- Ready to proceed to CellChat object creation and analysis

## Data Quality Requirements

### Seurat Object Requirements
**Essential elements**:
- **Cell type annotations**: Clear, consistent cell type labels
- **Normalized expression data**: Log-normalized or similar
- **Sufficient cell numbers**: At least 10-20 cells per cell type
- **Quality-controlled**: Doublets removed, low-quality cells filtered

**Metadata requirements**:
- Cell type column with meaningful names (not just numbers)
- Consistent naming (no typos or variations)
- All cells should have assigned cell types

### Gene Expression Considerations
**For optimal results**:
- Use normalized, scaled expression data
- Ensure ligand and receptor genes are expressed in your dataset
- Consider minimum expression thresholds
- Validate that expected signaling genes are present

```{tip}
Ensure your Seurat object has clear, consistent cell type annotations before loading. Cell types named "0, 1, 2..." should be renamed to biological identities like "T cells", "Macrophages", etc.
```

## Troubleshooting

**File won't load?**
- Verify file is a valid Seurat .rds object
- Check file isn't corrupted
- Ensure sufficient memory for large datasets
- Try re-saving Seurat object if issues persist

**No cell type annotations found?**
- Check metadata column names in your Seurat object
- Ensure cell types are assigned (not NA values)
- Verify column contains meaningful biological names

**Database loading fails?**
- Check internet connection for database download
- Verify species selection matches your data
- Try reloading if connection was interrupted

**Few interactions available?**
- May indicate species mismatch
- Could suggest limited gene coverage in dataset
- Consider if tissue/cell types express communication genes

```{warning}
Make sure your species selection exactly matches your experimental data. Using human database with mouse data (or vice versa) will result in very few or no detected interactions.
```

## Best Practices

### Before Loading
- **Rename clusters** to meaningful cell type names
- **Document your cell type assignments** and rationale
- **Verify data quality** with standard QC metrics
- **Consider cell type resolution** - too fine may fragment communication signals

### Species Selection
- **Double-check experimental species** in your lab notes
- **Verify gene naming conventions** in your data
- **Consider mixed experiments** carefully (use primary species)

### Database Preparation
- **Allow time for loading** - comprehensive database takes time to prepare
- **Check log messages** for any warnings or errors
- **Verify interaction counts** seem reasonable for your tissue type

## References

1. Jin et al., Inference and analysis of cell-cell communication using CellChat. Nature Communications, 2021. https://doi.org/10.1038/s41467-021-21246-9
2. CellChat Tutorial: https://htmlpreview.github.io/?https://github.com/jinworks/CellChat/blob/master/tutorial/CellChat-vignette.html