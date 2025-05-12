# Ligand-Receptor Analysis

## Overview
The Ligand-Receptor analysis module enables detailed investigation of cell-cell communication patterns by analyzing specific ligand-receptor interactions between different cell populations. This section guides you through the process of creating CellChat objects, running analyses, and generating visualizations.

## Create CellChat Objects

Begin by creating CellChat objects from your preprocessed data.

### Configuration Options
Choose how to group and analyze your cells:
- Group cells by:
  - Select the column from your metadata to define cell populations
  - Typically this would be your cell type annotations
  - Ensures proper grouping for interaction analysis
- Create subset by condition (Optional):
  - Enable comparison between different experimental conditions
  - When enabled, allows selection of a condition column
  - Useful for comparing treatments, time points, or disease states

### Process Steps
1. Select grouping variable (e.g., cell type)
2. Choose whether to create condition-based subsets
3. If using subsets:
   - Select the condition column
   - Objects will be created for each condition level
4. Click "Create Objects" to initialize CellChat analysis

## Analyze CellChat Objects

Run the analysis on your created objects.

### Analysis Configuration
- Select objects to analyze:
  - Choose one or multiple CellChat objects
  - Enables comparison between conditions if subsets were created
  - All selected objects will be processed simultaneously

### Analysis Steps
1. Select desired CellChat objects
2. Click "Run Analysis" to:
   - Identify significant interactions
   - Calculate interaction probabilities
   - Prepare data for visualization

## Visualization with Bubble Plots

Create visualizations of your analysis results.

### Plot Parameters
- Select CellChat object:
  - Choose which analysis results to visualize
  - Available objects depend on previous analysis steps
- Cell Type Selection:
  - Source cell types: Select cells producing ligands
  - Target cell types: Select cells expressing receptors
  - Multiple selections possible for both categories
- Interaction Filtering:
  - L-R pairs: Select specific ligand-receptor pairs
  - Signaling pathways: Filter by biological pathway
  - Threshold: Set significance threshold (default: 0.05)
  - Probability cutoff: Adjust interaction strength filter (0-1)

### Plot Interpretation
The bubble plot displays:
- X-axis: Source cell types
- Y-axis: Target cell types
- Bubble size: Interaction strength
- Color intensity: Significance level
- Only interactions passing threshold and cutoff values are shown

## Important Notes

### Tips for Optimal Analysis
- Start with a broad selection of cell types, then refine
- Adjust threshold and cutoff values iteratively
- Consider biological relevance when selecting L-R pairs
- Compare results between conditions when available

### Common Issues
- Missing cell type annotations
- Too stringent filtering resulting in no visible interactions
- Memory limitations with large datasets or many conditions
- Long processing times with multiple objects

### Best Practices
- Validate cell type annotations before analysis
- Start with default threshold values
- Document parameter choices for reproducibility
- Save plots for important findings