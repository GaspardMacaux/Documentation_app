# Ligand Activity Analysis

## Overview
This section analyzes and visualizes ligand-receptor interactions identified in your datasets.

## Analysis Process
1. **Set Analysis Parameters**
  * Set LogFC and p-value thresholds
  * Choose whether to include downregulated ligands
  * Select number of top targets to analyze
  * Set computational resources (cores)

2. **Run Analysis**
  * Click "Run Geneset & Ligand Analysis"
  * Analysis progress will be shown if enabled
  * Wait for completion

3. **View Results**
  
  **A. Ligand Activities Table**
  * Shows active ligands
  * Download available in CSV format
  
  **B. Prioritization Results**
  * Ranked list of interactions
  * Download table or complete analysis
  * Optional correlation calculations

## Visualization
**Circos Plot**
  * Shows ligand-target interactions
  * Set number of top interactions (default: 50)
  * Choose color palette
  * Export in publication quality

## Export Options
* Ligand Activities (CSV)
* Prioritization Table (CSV)
* Complete Analysis (RDS)
* Circos Plot (TIFF)

> **Tip:**
> Start with default thresholds (LogFC: 0.50, p-value: 0.05) and adjust based on results.

> **Note:**
> Including downregulated ligands will provide a more complete picture but may increase processing time.