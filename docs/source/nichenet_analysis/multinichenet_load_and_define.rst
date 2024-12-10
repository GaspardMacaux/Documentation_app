===============================
MultiNicheNet Analysis
===============================

### Overview

MultiNicheNet is a powerful extension of NicheNet that allows analysis of cell-cell communication across multiple conditions. Unlike NicheNet which compares two conditions, MultiNicheNet can analyze complex experimental designs with multiple groups, time points, or treatments.

### Detailed Step-by-Step Guide

#### Step 1: Data Preparation and Loading

1. **Required Files**

   A. **Expression Data**:
      - Format: Seurat or SingleCellExperiment object (.rds)
      - Must contain:
         * Gene expression matrix
         * Cell type annotations
         * Sample/condition information
         * Quality control metrics

   B. **Network Files**:
      - Ligand-receptor networks:
         * Human: zenodo.org/10229222
         * Mouse: zenodo.org/10229222
      - Ligand-target matrices:
         * Human: zenodo.org/7074291
         * Mouse: zenodo.org/7074291

2. **Loading Process**

   A. **Open Data Loading Menu**:
      - Click "Open Data Loading Menu"
      - System will display file selection interface

   B. **File Selection**:
      - Choose your expression data (.rds)
      - Select appropriate network files
      - Verify file formats match species

   C. **Validation**:
      - System checks file integrity
      - Verifies data structure
      - Confirms metadata presence
      - Reports any issues found

#### Step 2: Metadata Parameter Definition

1. **Sample ID Selection**
   
   A. **Purpose**:
      - Uniquely identifies each sample
      - Links cells to experimental conditions
      - Essential for batch effect control

   B. **How to Select**:
      - From dropdown menu, choose column containing sample identifiers
      - Verify each sample has unique ID
      - Ensure IDs match your experimental design

   C. **Common Issues**:
      - Missing sample information
      - Duplicate IDs
      - Inconsistent naming

2. **Group ID Configuration**

   A. **Purpose**:
      - Defines experimental conditions
      - Groups samples by treatment/state
      - Enables statistical comparisons

   B. **Selection Process**:
      - Choose column containing group information
      - Verify all samples have group assignments
      - Check group names match your design

   C. **Examples**:
      - Treatment vs Control
      - Time points (Day1, Day2, etc.)
      - Disease states
      - Genetic conditions

3. **Cell Type ID Selection**

   A. **Purpose**:
      - Identifies cell populations
      - Enables population-specific analysis
      - Required for sender/receiver definition

   B. **How to Choose**:
      - Select column with cell type annotations
      - Verify annotations are consistent
      - Check population sizes

   C. **Requirements**:
      - Clear cell type labels
      - Sufficient cells per type
      - Biological relevance

#### Step 3: Contrast Definition

1. **Understanding Contrasts**

   A. **Purpose**:
      - Defines comparisons of interest
      - Structures statistical analysis
      - Guides result interpretation

   B. **Types of Contrasts**:
      - Simple (A vs B)
      - Multiple (A vs B vs C)
      - Complex (A vs [B+C]/2)
      - Time series

2. **Setting Up Contrasts**

   A. **Group Selection**:
      - Choose groups to compare
      - Order determines contrast direction
      - Multiple selections possible

   B. **Formula Generation**:
      - System creates contrast formula
      - Displays in mathematical notation
      - Shows comparison structure

   C. **Validation**:
      - Check formula accuracy
      - Verify group selection
      - Confirm comparison logic

### Important Considerations

#### 1. Data Quality
- Minimum cells per group: >100 recommended
- Even group sizes preferred
- Clean annotations required
- Quality control metrics checked

#### 2. Experimental Design
- Balanced design preferred
- Sufficient replication
- Clear control groups
- Logical comparisons

#### 3. Technical Requirements
- Memory: 16GB minimum
- Storage: 10GB free space
- Processing: Multi-core recommended

### Troubleshooting Common Issues

Problem | Cause | Solution | Prevention
--------|-------|----------|------------
Missing groups | Incorrect column | Check metadata | Verify before analysis
Error in contrast | Invalid formula | Revise selection | Test simple contrasts first
Memory error | Large dataset | Reduce scope | Check requirements
Failed loading | Format issue | Check file type | Use provided templates

### Next Steps
After completing these steps:
1. Run analysis
2. Review results
3. Generate visualizations
4. Export findings

### References

1. Browaeys, R., et al. (2020) Nature Methods 17:159-162.
2. MultiNicheNet documentation: github.com/saeyslab/multinichenet
3. Network resources: zenodo.org/7074291