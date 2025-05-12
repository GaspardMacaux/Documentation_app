# Circos Plot Visualization

## Overview
The Circos plot shows interactions between cells and genes in a circular format. It helps visualize which cells are sending signals and which genes are responding.

## Step 1: Set Up Cell Connections
**Click "Assign Ligands"**
* This identifies which cells are producing signals
* System automatically finds signaling molecules
* Wait for confirmation message

**Set Up Target Links:**
* Enter target type (e.g., "LCMV-DE")
* Set link cutoff (default: 0.4)
* Click "Define Links"
* Controls which connections to show

## Step 2: Customize Appearance
**Choose Colors:**
* Select colors for each cell type
* Choose receptor color
* Colors help distinguish different cells

**Adjust Layout:**
* Link size: Controls connection thickness
* Enable transparency if needed
* Text position: Inside/Outside/Both
* Gap between sections: 1-10 degrees

## Step 3: Generate and Export
**Generate Plot:**
* Click "Generate Circos Plot"
* Check visualization
* Adjust settings if needed
* Regenerate as necessary

**Export Options:**
* Set resolution (DPI)
* Click "Download Plot"
* Save as TIFF file

## Recommended Settings
**For Clear Visualization:**
* Link size: 1.0
* Text size: 0.6
* Gap: 1 degree
* DPI: 300 (minimum for publication)

**For Dense Data:**
* Enable transparency
* Reduce number of top receptors
* Increase gap between sectors
* Adjust text position to "Outside"

> **Tip:**
> Start with default settings and adjust based on your needs.

> **Note:**
> Use 300+ DPI for publication-quality images.

## References
* Gu, Z. et al. Bioinformatics 30, 2811-2812 (2014)
* Krzywinski, M. et al. Genome Res. 19, 1639-1645 (2009)