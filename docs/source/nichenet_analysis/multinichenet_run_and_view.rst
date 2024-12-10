===============================
Run and View Results
===============================

### Overview

This section allows you to set parameters and execute the MultiNicheNet analysis across your datasets. The interface provides detailed control over expression thresholds, statistical parameters, and computational resources.

### Analysis Parameters

#### Expression Thresholds

1. **Minimum Sample Proportion**
   - Default: 0.50 (50%)
   - Range: 0-1
   - Purpose: Defines minimum fraction of samples where gene must be expressed
   - Impact: Higher values increase reliability but may miss rare signals

2. **Fraction Cutoff**
   - Default: 0.05 (5%)
   - Range: 0-1
   - Purpose: Minimum fraction of cells expressing a gene
   - Impact: Filters out low-abundance transcripts

3. **LogFC Threshold**
   - Default: 0.50
   - Range: 0-∞
   - Purpose: Minimum log fold change for differential expression
   - Impact: Controls effect size sensitivity

#### Statistical Controls

1. **P-value Settings**
   
   A. **P-value Threshold**
      - Default: 0.05
      - Range: 0-1
      - Purpose: Statistical significance cutoff
      - Impact: Controls false positive rate

   B. **Empirical P-values**
      - Optional: Checkbox
      - Purpose: Uses permutation-based p-values
      - Impact: More robust but computationally intensive
      - Recommended: For small sample sizes

   C. **P-value Adjustment**
      - Optional: Checkbox
      - Purpose: Corrects for multiple testing
      - Methods: Benjamini-Hochberg by default
      - Impact: Controls false discovery rate

#### Analysis Configuration

1. **Target Gene Selection**
   - Parameter: Top N target genes
   - Default: 250
   - Range: 1-∞
   - Purpose: Number of target genes to analyze per ligand

2. **Computational Resources**
   
   A. **Parallel Processing**
      - Parameter: Number of cores
      - Default: 8
      - Range: 1-available cores
      - Impact: Analysis speed and memory usage

   B. **Minimum Cells**
      - Default: 10
      - Range: 1-∞
      - Purpose: Minimum cells required per group
      - Impact: Statistical reliability

### Execution Steps

1. **Initial Calculations**
   A. Click "Calculate Abundance & Expression"
      - Computes cell type abundance
      - Analyzes gene expression patterns
      - Prepares data for DE analysis

2. **Main Analysis**
   A. Click "Run Expression & DE Analysis"
      - Performs differential expression
      - Calculates ligand activities
      - Generates result matrices

### Results Visualization

#### DE P-values Distribution
- Plot type: Histogram
- Y-axis: Frequency
- X-axis: P-value ranges
- Purpose: Quality control and bias detection

### Output Options

1. **Plot Downloads**
   - Format: TIFF
   - Resolution: Publication quality
   - Usage: Manuscript figures
   - Content: P-value distributions

### Quality Control

1. **Check Points**
   - P-value distribution shape
   - Number of significant genes
   - Effect size distribution
   - Cell type representation

2. **Warning Signs**
   - Uniform p-value distribution
   - Too many/few significant genes
   - Extreme effect sizes
   - Missing cell populations

### Performance Considerations

1. **Memory Usage**
   - Scales with:
     * Dataset size
     * Number of comparisons
     * Target gene count
     * Parallel processes

2. **Processing Time**
   - Affected by:
     * Core count
     * Sample size
     * Parameter choices
     * Statistical methods

### Tips for Optimal Analysis

1. **Parameter Selection**
   - Start conservative
   - Adjust based on results
   - Document changes
   - Validate findings

2. **Resource Management**
   - Monitor memory usage
   - Adjust core count as needed
   - Save intermediate results
   - Plan for long runs

### Common Issues and Solutions

Problem | Cause | Solution | Prevention
--------|-------|----------|------------
Memory Error | Too many cores | Reduce core count | Monitor usage
Long Runtime | Large target set | Reduce gene count | Start small
Poor Statistics | Low cell count | Adjust thresholds | Check QC first
Failed Analysis | Parameter conflict | Reset defaults | Test parameters

### Next Steps
After analysis completion:
1. Examine p-value distribution
2. Review effect sizes
3. Export significant results
4. Generate visualizations