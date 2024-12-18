===============================
DoubletFinder
===============================

Overview
DoubletFinder is a tool used to identify and remove cell doublets from single-cell RNA sequencing data. Doublets occur when two cells are captured and sequenced together, potentially confounding downstream analysis.

Parameters and Settings

pK Identification
- **Purpose**: Determines optimal pK value
- **Process**: 
 * Tests multiple pK values
 * Measures mean-variance relationships
 * Identifies optimal parameter
 * pK range typically: 0.01-0.3

nExp Parameter
- **Definition**: Expected number of doublets
- **Calculation**:
 * Based on cell loading density
 * 10X standard: ~0.8% per 1000 cells
 * Example: 10,000 cells ≈ 80 doublets

pN Parameter
- **Purpose**: Sets proportion of artificial doublets
- **Default**: 0.25
- **Range**: Usually 0.15-0.3

Running DoubletFinder

1. **Parameter Optimization**
  - Click "Find optimal pK"
  - Review pK vs BCmvn plot
  - Select best pK value

2. **Doublet Detection**
  - Enter expected doublet rate
  - Run DoubletFinder
  - Review results

3. **Results Visualization**
  - UMAP plot with doublets highlighted
  - Statistics summary
  - Option to remove identified doublets

.. tip::
  * Start with default parameters
  * Adjust based on experimental design
  * Consider biological expectations
  * Document chosen parameters

.. warning::
  * Check cell numbers carefully
  * Verify doublet rate expectations
  * Don't overfilter rare populations
  * Validate removed cells

QC Metrics

Key Outputs
- Doublet scores
- Doublet classifications
- Visualization plots
- Summary statistics

Validation Approaches
- Check known doublet markers
- Review cell numbers
- Examine cluster distributions
- Verify rare populations

References

1. McGinnis, C.S., Murrow, L.M. & Gartner, Z.J. DoubletFinder: Doublet Detection in Single-Cell RNA Sequencing Data Using Artificial Nearest Neighbors. Cell Syst 8, 329-337.e4 (2019).

2. https://github.com/chris-mcginnis-ucsf/DoubletFinder

