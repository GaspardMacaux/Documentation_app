===============================
Circos Plot Visualization
===============================

### Overview
The Circos plot module visualizes complex ligand-target interactions across cell populations using circular diagrams.

### Step-by-Step Process

#### 1. Ligand Assignment
- **Purpose**: Map ligands to sender cells
- **Method**: Expression-based assignment
- **Assignment Function**: 
 * Uses mean expression
 * Adds 0.5 standard deviations
 * Ensures cell type specificity

#### 2. Link Definition
- **Target Type**:
 * User-defined category (e.g. "LCMV-DE") 
 * Indicates target gene set
 * Must match analysis context

- **Link Cutoff (0-1)**:
 * Controls interaction strength filtering 
 * Default: 0.4
 * Higher = stricter filtering
 * Lower = more connections shown

#### 3. Visual Customization

##### Color Settings
- **Donor Colors**:
 * Individual colors per sender
 * Automatically generated defaults
 * Custom color selection
 * Helps distinguish populations

- **Receiver Color**:
 * Single color for targets
 * Default: Grey (#999999)
 * Customizable
 * Contrasts with donors

##### Plot Parameters
- **Transparency**: 
 * Toggle for link visibility
 * Helps with dense plots
 * Default: OFF
 * Value: 0.3-0.7

- **Link Size (0.1-2.0)**:
 * Controls connection width
 * Default: 1.0
 * Affects readability
 * Scale with plot size

- **Text Settings**:
 * Size: 0.1-2.0 (Default: 0.6)
 * Position: Inside/Outside/Both
 * Affects label clarity
 * Adjusts automatically

#### 4. Advanced Options
- **Top Receptors**: 1-100 (Default: 20)
- **Sort Mode**: Default/Ascending/Descending
- **Sector Gap**: 0-10 degrees (Default: 1)
- **Plot Resolution**: 72-1200 DPI

### Plot Generation

#### Process Steps
1. Ligand assignment
2. Link definition
3. Color selection
4. Parameter setting
5. Plot generation
6. Export (optional)

#### Export Options
- Format: TIFF
- Size: 10x8 inches
- Resolution: User-defined DPI
- Compression: LZW

### Parameter Guidelines

Setting | Range | Default | Impact
--------|-------|---------|--------
Link Cutoff | 0-1 | 0.4 | Interaction filtering
Text Size | 0.1-2 | 0.6 | Label readability
Link Size | 0.1-2 | 1.0 | Connection visibility
Gap Degree | 0-10 | 1 | Sector separation

### Best Practices

#### Color Selection
- Use contrasting colors
- Maintain readability
- Consider colorblind accessibility
- Match biological relevance

#### Layout Optimization
- Balance label size
- Adjust transparency for density
- Control number of targets
- Consider plot purpose

### Troubleshooting

Problem | Cause | Solution
--------|-------|----------
Overlapping text | Too many elements | Reduce targets/increase gap
Unclear links | Low contrast | Adjust colors/transparency
Missing labels | Size/position | Modify text parameters
Poor resolution | Low DPI | Increase export DPI

### References

1. Gu, Z. et al. circlize implements and enhances circular visualization in R. Bioinformatics 30, 2811-2812 (2014).

2. Krzywinski, M. et al. Circos: an Information Aesthetic for Comparative Genomics. Genome Res. 19, 1639-1645 (2009).