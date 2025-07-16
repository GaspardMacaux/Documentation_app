# Circle Plots Analysis

## Overview
Circle plots provide powerful visualization methods to understand cell-cell communication networks from different perspectives. This section offers three complementary approaches: chord diagrams for specific interactions, global network overviews, and cell type-focused communication patterns.

## What You'll Do on This Tab
- **Create chord diagrams** showing directional communication between specific cell types
- **Generate global network plots** displaying overall communication patterns
- **Analyze cell type-specific signals** focusing on individual populations
- **Customize visualizations** for optimal display and interpretation

## Visualization Methods Available

### 1. Chord Plot - Ligand-Receptor Interactions

**When to use**: Examine specific directional communications between selected cell types

**What it shows**:
- **Chord width**: Strength of communication between cell types
- **Direction**: Which cell type sends signals to which
- **Color coding**: Different cell types have distinct colors
- **Specific interactions**: Focus on particular ligand-receptor pairs

#### Setup Process
**Data Selection**:
- **CellChat object**: Choose which analysis results to visualize
- **Sender cell types**: Select cells that produce ligands
- **Receiver cell types**: Select cells that express receptors
- Can focus on specific cell type pairs of interest

**Parameters**:
- **Min probability**: Minimum interaction strength to display (default: 0.05)
- **Label distance**: How far labels appear from the circle
- **Label size**: Text size for cell type names

**Display Settings**:
- **Plot size**: Diameter in pixels for optimal viewing
- **Custom colors**: Optional cell type-specific colors
- **Export options**: Multiple formats available

**Generate Plot**:
- Click "Generate Plot" to create chord diagram
- Shows directional communication flows between selected cell types

### 2. Network Overview - Global Communication

**When to use**: Get comprehensive view of all communication patterns in your dataset

**What it shows**:
- **Cell type nodes**: Circles representing each cell type
- **Node size**: Proportional to cell type abundance
- **Edge thickness**: Communication strength between cell types
- **Network structure**: Overall communication topology

#### Configuration Options
**Metric Selection**:
- **Number of interactions**: Shows how many different signals exist
- **Interaction weights**: Shows total communication strength
- Choose based on whether you want diversity vs intensity

**Visual Parameters**:
- **Cell type size**: Adjust node sizes (5-30 range)
- **Max edge width**: Control maximum connection thickness
- **Label size**: Text size for cell type names
- **Plot margin**: Space around the network

**Display Control**:
- **Display size**: Plot dimensions in pixels
- Adjust based on number of cell types for optimal viewing

#### Interpretation Guide
- **Central nodes**: Cell types involved in many communications
- **Thick edges**: Strong communication channels
- **Isolated nodes**: Cell types with limited communication
- **Network clusters**: Groups of highly interconnected cell types

### 3. Cell Type Focus - Outgoing & Incoming Signals

**When to use**: Examine communication patterns for specific cell types of interest

**What it shows**:
- **Outgoing signals**: What messages a cell type sends to others
- **Incoming signals**: What messages a cell type receives from others
- **Individual plots**: Separate visualization for each selected cell type

#### Setup Configuration
**Cell Type Selection**:
- **Select cell types**: Choose specific populations to analyze
- **Multiple selection**: Analyze several cell types simultaneously
- **Signal direction**: Choose "Outgoing" or "Incoming" focus

**Outgoing Signals (as sender)**:
- Shows which cell types receive signals from your selected type
- Edge thickness indicates communication strength
- Reveals the "influence" of your cell type

**Incoming Signals (as receiver)**:
- Shows which cell types send signals to your selected type
- Reveals what "inputs" your cell type receives
- Identifies potential regulatory cell types

**Layout Parameters**:
- **Label size**: Text size for readability
- **Plot margin**: Space around individual plots
- **Columns**: Number of plots per row (1-6)
- **Plot height**: Individual plot dimensions

![](../_static/images/cellchat_analysis/cellchat_circleplot.png)


