NicheNet Results Visualization
=================================

### Overview
The results section provides comprehensive visualization and analysis options for understanding ligand-receptor interactions and their downstream effects.

### Available Output Types

#### 1. Ligand Activities
- **Purpose**: Shows prioritized ligands and their activity scores
- **Content**:
  * Ligand names
  * Activity scores
  * Statistical measures
  * Regulatory potential

- **Interpretation**:
  * Higher scores = stronger influence
  * Prioritize top-scoring ligands
  * Consider biological relevance
  * Check expression patterns

#### 2. Top Ligands & Targets
- **Top Ligands Display**:
  * Most influential ligands
  * Based on activity scores
  * Ranked by importance
  * Expression-filtered

- **Top Targets View**:
  * Affected target genes
  * Expression changes
  * Regulatory strength
  * Pathway involvement

#### 3. Visualization Plots

A. **Ligand Expression Dotplot**
- **Features**:
  * Cell type-specific expression
  * Dot size = percentage expressing
  * Color = expression level
  * Cluster organization

- **Settings**:
  * Resolution: 72-1200 DPI
  * Export format: TIFF
  * Size adjustable
  * Color schemes

B. **Differential Expression Heatmap**
- **Content**:
  * Expression changes
  * Condition comparison
  * Statistical significance
  * Cluster patterns

- **Parameters**:
  * Color scale
  * Clustering options
  * Label settings
  * Size control

C. **Ligand-Target Heatmap**
- **Shows**:
  * Regulatory connections
  * Interaction strengths
  * Expression patterns
  * Network structure

- **Customization**:
  * Clustering methods
  * Color gradients
  * Size parameters
  * Label options

D. **Ligand-Receptor Heatmap**
- **Displays**:
  * Direct interactions
  * Expression correlation
  * Cell type specificity
  * Interaction strength

- **Controls**:
  * Resolution settings
  * Color schemes
  * Size adjustment
  * Label management

#### 4. Data Matrices

A. **Ligand-Target Matrix**
- **Structure**:
  * Rows = targets
  * Columns = ligands
  * Values = interaction scores
  * Binary connections

- **Usage**:
  * Network analysis
  * Pattern identification
  * Pathway mapping
  * Validation

B. **Ligand-Target Dataframe**
- **Content**:
  * Detailed interactions
  * Statistical measures
  * Expression data
  * Metadata

- **Applications**:
  * Further analysis
  * Data export
  * Result validation
  * Documentation

### Export Options

#### 1. Image Export
- **Formats**:
  * TIFF (default)
  * Resolution: 72-1200 DPI
  * Width: 8 inches
  * Height: 6 inches

- **Settings**:
  * Compression: LZW
  * Quality control
  * Size adjustment
  * Format validation

#### 2. Data Export
- **Tables**:
  * CSV format
  * Complete data
  * Headers included
  * Standardized format

- **Text Files**:
  * Gene lists
  * Parameters
  * Statistics
  * Annotations

### Best Practices

#### 1. Resolution Selection
- **Print Quality**: >300 DPI
- **Screen Display**: 72-150 DPI
- **Publication**: 600+ DPI
- **Web Use**: 72-96 DPI

#### 2. Data Interpretation
- Validate key findings
- Cross-reference literature
- Check biological relevance
- Document parameters

#### 3. Quality Control
- Verify image quality
- Check data completeness
- Validate statistics
- Confirm cell types

### Troubleshooting

Problem | Cause | Solution
--------|-------|----------
Low resolution images | DPI too low | Increase DPI setting
Missing data | Export error | Check file format
Unclear patterns | Poor contrast | Adjust color scheme
Export fails | Memory limits | Reduce image size
Incomplete labels | Space constraints | Adjust plot size
