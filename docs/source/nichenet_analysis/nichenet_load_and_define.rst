===============================
NicheNet Analysis
===============================

### Overview: Principles and Theory

NicheNet is a computational method for studying cell-cell communication through ligand-receptor interactions. It predicts which ligands, secreted by sender cells, influence gene expression in receiver cells.

#### Core Concepts

1. **Cell-Cell Communication**
  - **Sender Cells**:
    * Produce and secrete ligands
    * Can be multiple cell types
    * Example: Fibroblasts secreting growth factors

  - **Receiver Cells**:
    * Express receptors
    * Respond to ligands
    * Show gene expression changes
    * Example: Epithelial cells responding to signals

2. **Interaction Types**
  - **Direct**:
    * Ligand-receptor binding
    * Cell surface contact
    * Immediate response

  - **Indirect**:
    * Downstream signaling
    * Gene expression changes
    * Cellular state changes

### Required Data Files: Detailed Structure

#### 1. Seurat Object (.rds)
- **Content Requirements**:
 * Expression matrix
 * Cell metadata
 * Cluster information
 * Experimental conditions

- **Quality Criteria**:
 * Normalized data
 * Cell type annotations
 * Clear condition labels
 * Sufficient cell numbers (>100 per group)

#### 2. Network Files

A. **Ligand-Receptor Network**
  - **Structure**:
    * Ligand column (gene names)
    * Receptor column (gene names)
    * Interaction scores/weights
    * Source annotation

  - **Format Requirements**:
    * .rds file
    * Standard gene nomenclature
    * No duplicates
    * Validated interactions

B. **Ligand-Target Matrix**
  - **Content**:
    * Ligands as columns
    * Target genes as rows
    * Regulatory scores
    * Prior knowledge integration

  - **Technical Specs**:
    * Sparse matrix format
    * Normalized scores (0-1)
    * Complete gene coverage
    * Validated interactions

C. **Weighted Networks**
  - **Components**:
    * Network topology
    * Edge weights
    * Node attributes
    * Interaction types

### Step-by-Step Analysis Guide

#### 1. Data Loading Phase

A. **Seurat Object Upload**
  - Click "Open Data Loading Menu"
  - Select .rds file
  - System checks:
    * File integrity
    * Data structure
    * Memory requirements
    * Gene name format

B. **Network Files Upload**
  - Upload all three required files
  - Validation process:
    * Format checking
    * Gene name standardization
    * Network compatibility
    * Matrix dimensions

#### 2. Population Definition

A. **Cell Identity Column Selection**
  - Choose metadata column containing cell types
  - Requirements:
    * Clear labels
    * Consistent naming
    * Sufficient representation
    * Biological relevance

B. **Sender Cell Selection**
  - Multiple selection enabled
  - Considerations:
    * Known ligand producers
    * Cell type markers
    * Biological context
    * Sample size

C. **Receiver Cell Selection**
  - Multiple selection possible
  - Key factors:
    * Expected responders
    * Receptor expression
    * State changes
    * Population size

#### 3. Parameter Configuration

A. **Condition Parameters**

1. **Condition Column**
  - Purpose: Define experimental groups
  - Requirements:
    * Clear labeling
    * Balanced groups
    * Sufficient replication
    * Controlled variables

2. **Condition of Interest**
  - Definition: Treatment/experimental group
  - Considerations:
    * Sample size
    * Quality metrics
    * Technical variables
    * Biological replicates

3. **Reference Condition**
  - Purpose: Control/baseline
  - Requirements:
    * Matched controls
    * Similar quality
    * Appropriate timing
    * Technical consistency

B. **Expression Parameters**

1. **Expression Percentage Threshold**
  - Range: 0.01-1.0
  - Default: 0.05
  - Impact:
    * Lower (<0.05):
      - Captures rare events
      - More false positives
      - Higher computation time
      - Good for exploratory analysis
    * Medium (0.05-0.1):
      - Balanced detection
      - Standard analysis
      - Recommended default
      - Good reproducibility
    * Higher (>0.1):
      - Strong signals only
      - Fewer false positives
      - Faster computation
      - May miss subtle effects

2. **Top Ligands Parameter**
  - Range: 1-200
  - Default: 50
  - Effects:
    * Lower numbers (<30):
      - Focus on strong signals
      - Faster analysis
      - More stringent
      - May miss important factors
    * Medium range (30-70):
      - Balanced approach
      - Good coverage
      - Reasonable computation
      - Recommended for most analyses
    * Higher numbers (>70):
      - Comprehensive analysis
      - Longer computation
      - More noise
      - Good for discovery

### Analysis Execution

#### 1. Running the Analysis
- Click "Run NicheNet Analysis"
- Progress monitoring:
 * Data preprocessing
 * Network analysis
 * Score calculation
 * Results compilation

#### 2. Quality Control
- Automatic checks:
 * Data completeness
 * Parameter validation
 * Cell numbers
 * Expression thresholds

#### 3. Error Handling
- Common issues:
 * Memory limitations
 * Missing data
 * Parameter conflicts
 * Network incompatibility

### Results Interpretation

#### 1. Primary Outputs
- Ligand rankings
- Target predictions
- Interaction scores
- Statistical measures

#### 2. Visualization Options
- Network plots
- Expression heatmaps
- Interaction matrices
- Score distributions

#### 3. Validation Approaches
- Known interactions
- Literature comparison
- Experimental validation
- Statistical significance

### Best Practices and Tips

#### 1. Analysis Design
- Start with known interactions
- Use biological replicates
- Include positive controls
- Consider sample size

#### 2. Parameter Selection
- Begin with defaults
- Adjust based on biology
- Document all changes
- Validate key findings

#### 3. Quality Control
- Check cell numbers
- Verify annotations
- Monitor batch effects
- Validate results

### Troubleshooting Guide

Problem | Cause | Solution | Prevention
--------|-------|----------|------------
No significant ligands | Threshold too high | Lower expression threshold | Start with default parameters
Memory errors | Large dataset | Reduce parameter scope | Check requirements beforehand
Missing interactions | Poor annotation | Update cell labels | Validate annotations early
Slow computation | Too many parameters | Focus analysis | Optimize parameter selection
Network errors | Format mismatch | Check file formats | Use provided templates

### References and Resources

References
----------

1. Browaeys, R., Saelens, W. & Saeys, Y. NicheNet: modeling intercellular communication by linking ligands to target genes. Nat Methods 17, 159–162 (2020). https://doi.org/10.1038/s41592-019-0667-5

2. Bhttps://github.com/saeyslab/nichenetr

3. Network Resources:
   - Human/Mouse Networks: https://doi.org/10.5281/zenodo.7074291
   - Expression Data: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144357
   - Code Repository: https://github.com/saeyslab/nichenetr
