# Circle Plots Analysis

## Overview
The Circle Plots module provides three different visualization methods for analyzing cell-cell communication patterns:
1. Global Circle Plot: Overview of all cell type interactions
2. Cell Type Specific Plots: Detailed view of selected cell type communications
3. Chord Diagram: Directional communication patterns between specific cell groups

## Global Circle Plot
### Purpose
Visualizes the overall communication pattern between all cell types in your dataset, providing a comprehensive view of cellular interactions.

### Configuration Options
- **CellChat Object Selection**:
  - Choose the analyzed CellChat object to visualize
  - Each object represents a specific condition or analysis state

- **Plot Parameters**:
  - **Plot type**:
    - Number of interactions: Shows count of significant interactions
    - Interaction weights: Displays strength of communications
  - **Font Size**: Adjust text visibility (0.1-2.0)
  - **Plot resolution**: Set DPI for export quality (72-1200)
  - **Margin Size**: Control plot spacing (0.1-1.0)

### Visualization Options
- **Generate Plot**: Creates the circle plot visualization
- **Download Plot**: Save high-resolution image
- **Interactive display**: View plot with automatic size adjustment

## Cell Type Specific Plots
### Purpose
Creates focused visualizations for selected cell types, allowing detailed examination of their communication patterns.

### Configuration Options
- **CellChat Object**: Select analysis results to visualize
- **Cell Type Selection**:
  - Multiple cell types can be selected
  - Filtered view of specific cell populations
  
### Plot Parameters
- **Font Size**: Adjust text clarity (0.1-2.0)
- **Margin Size**: Control spacing between plots (0.1-1.0)
- **Plot resolution**: Set export quality (72-1200)

### Output Features
- Multiple plots generated simultaneously
- Each selected cell type gets dedicated visualization
- Downloadable high-resolution images

## Chord Diagram Analysis
### Purpose
Visualizes directional communication patterns between specific sender and receiver cell populations with pathway-specific information.

### Configuration Options
- **CellChat Object**: Select analysis dataset
- **Cell Group Selection**:
  - **Sender Cell Types**: Select source populations
  - **Receiver Cell Types**: Select target populations
  - Flexible multiple selection for both categories

- **Interaction Filtering**:
  - **Signaling pathways**: Filter by specific pathways
  - **L-R pairs**: Optional selection of specific interactions
  - **Display Mode**:
    - Sending from selected: Focus on outgoing signals
    - Receiving by selected: Focus on incoming signals

### Technical Parameters
- **Plot resolution**: Adjust export quality (72-1200)
- Automatic size adjustment for visualization
- High-resolution export option

## Best Practices
### General Tips
- Start with Global Circle Plot for overview
- Use Cell Type Specific Plots for detailed analysis
- Apply Chord Diagram for pathway-specific investigations

### Optimization Guidelines
- **Resolution Settings**:
  - Use 300 DPI for screen viewing
  - Increase to 600+ DPI for publication
  
- **Font Size Adjustment**:
  - Start with default 0.4
  - Adjust based on cell type number
  - Increase for presentations

- **Cell Type Selection**:
  - Limit to 5-8 types for clear visualization
  - Group similar cell types if necessary
  - Consider biological relevance

### Common Issues
- Overlapping labels with many cell types
- Export file size with high DPI
- Visual clarity with multiple pathways

### Recommendations
- Save plots at multiple resolutions
- Document parameter settings
- Consider plot purpose when selecting visualization type
- Use consistent settings across analysis