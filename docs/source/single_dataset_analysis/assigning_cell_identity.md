# Assigning Cell Identity

## Overview
This section allows you to assign biological names to your clusters based on their gene expression patterns. Instead of having clusters named "0, 1, 2, 3...", you can rename them to meaningful cell types like "Muscle stem cells", "Myoblasts", "Myocytes", etc. This step transforms your technical clustering results into biological interpretation.

## What You'll Do on This Tab
- **Rename clusters** with biologically meaningful names based on marker gene expression
- **Customize visualization** with appropriate colors for each cell type
- **Validate assignments** using expression plots to confirm your cell type identifications
- **Create final annotated plots** ready for publication or presentation

## Cluster Renaming Process

### How to Rename Clusters

![](../_static/images/single_dataset_analysis/menu_assinging_single.tiff)

**Step 1: Identify Your Cluster**
- Use the "Select cluster" dropdown to choose which cluster to rename
- The current name (usually a number) will be shown

**Step 2: Choose a Biological Name**
- Enter the new cell type name in "New name" field
- Use standard biological nomenclature (e.g., "Satellite cells", "Myofibroblasts")
- Be specific and consistent with naming conventions

**Step 3: Apply the Change**
- Click "Apply Name" to rename the selected cluster
- The change is immediately applied to all visualizations
- You can rename multiple clusters by repeating this process

### Merging Clusters
**Automatic Merging**
- If you give two different clusters the same name, they will automatically merge
- Example: Rename cluster "0" to "Myoblasts" and cluster "3" to "Myoblasts" → they become one group
- Useful when clustering split one cell type into multiple clusters

## Visualization Customization

### Plot Settings
**Customize Appearance**
- **Plot title**: Change the main title (default: "UMAP Final")
- **Label size**: Adjust cluster name text size for readability
- **Point size**: Change cell dot size for better visibility

### Color Management
**Assign Custom Colors**
- Select cluster from "Select cluster" dropdown
- Choose appropriate color using the color picker
- Click "Update Color" to apply the new color
- Colors help distinguish cell types and create publication-ready figures

**Color Strategy Tips**
- Use biologically meaningful colors (e.g., red for muscle, blue for immune cells)
- Ensure sufficient contrast between similar cell types
- Keep colors consistent across related analyses

![](../_static/images/single_dataset_analysis/renaming_single.tiff)

## Validation Tools

### Interactive UMAP Display
**Main Visualization**
- Shows your clusters with current names and colors
- Interactive plot allows zooming and exploration
- Updates automatically when you rename clusters or change colors
- Hover over cells to see detailed information

### Alternative Plot Validation
**Expression Plot Selector**
- Choose from: FeaturePlot, VlnPlot, DotPlot, or RidgePlot
- Use these plots to validate your cell type assignments
- Check if marker genes are expressed in the clusters you expect

![](../_static/images/single_dataset_analysis/feature_renaming_single.tiff)

**How to Use for Validation**
1. **Select plot type** that best shows your validation genes
2. **Examine expression patterns** to confirm cluster identity
3. **Adjust naming** if expression doesn't match expected cell type
4. **Iterate** until assignments make biological sense

## Recommended Workflow

### Step 1: Prepare for Annotation
- Have a list of known marker genes for your tissue/system
- Research expected cell types for your experimental context
- Note the expression patterns you observed in previous visualization steps

### Step 2: Start with Clear Clusters
- Begin with clusters showing strong, specific marker expression
- Rename obvious cell types first (e.g., clear muscle vs immune signatures)
- Leave ambiguous clusters for later analysis

### Step 3: Systematic Validation
- For each renamed cluster, validate using multiple marker genes
- Use violin plots to check marker specificity
- Use feature plots to see spatial distribution
- Ensure markers are specific to your assigned cell type

### Step 4: Handle Difficult Cases
**Ambiguous Clusters**
- May represent transitional states or mixed populations
- Consider names like "Progenitor cells" or "Transitional state"
- Use additional markers or trajectory analysis for clarification

**Similar Cell Types**
- Use subtle naming differences (e.g., "Myoblasts_early", "Myoblasts_late")
- Choose distinct colors for visual separation
- Document the distinguishing features

### Step 5: Final Review
- Check that all clusters have meaningful biological names
- Ensure color scheme is publication-appropriate
- Validate major cell types with established markers
- Document your rationale for future reference

```{tip}
Start by validating your cell type assignments with well-established marker genes. Use the validation plots extensively - if a marker gene isn't expressed where you expect, reconsider your cell type assignment.
```

## Best Practices

### Naming Conventions
- Use standard cell type terminology from literature
- Be specific enough to be informative
- Avoid overly long names that clutter plots
- Consider using abbreviations for complex names

### Validation Strategy
- Always validate with multiple markers per cell type
- Check both positive markers (expressed in your cell type) and negative markers (not expressed)
- Use different plot types to see expression from multiple angles
- Cross-reference with published single-cell atlases when available

### Color Choices
- Consider colorblind-friendly palettes
- Use intuitive colors when possible (red for muscle, green for immune)
- Ensure adequate contrast for publication
- Save color schemes for consistency across figures

```{warning}
Don't rush the annotation process. Incorrect cell type assignments will affect all downstream analyses and interpretations. Always validate assignments with multiple markers and different visualization methods.
```

## Common Challenges

**Too Many Small Clusters?**
- Consider merging related clusters with similar marker expression
- May indicate over-clustering that split single cell types
- Use biological knowledge to guide merging decisions

**Clusters with Mixed Markers?**
- May represent doublets that weren't filtered
- Could be transitional states between cell types
- Consider additional quality control or trajectory analysis

**No Clear Markers for Some Clusters?**
- May need deeper sequencing or more cells
- Could represent rare or novel cell populations
- Consider leaving as "Unknown" rather than forcing incorrect assignment

## Next Steps

After successful cell type assignment:
- Proceed to detailed marker gene analysis for each cell type
- Consider trajectory analysis to understand cell relationships
- Export annotated data for further specialized analyses
- Document your annotations for publication and data sharing