==========================
Circos Plot Visualization
==========================

Overview
--------
The Circos plot shows interactions between cells and genes in a circular format. It helps visualize which cells are sending signals and which genes are responding.

Creating Your Plot
----------------

Step 1: Set Up Cell Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Click "Assign Ligands"
   * This identifies which cells are producing signals
   * System automatically finds signaling molecules
   * Wait for confirmation message

2. Set Up Target Links
   * Enter target type (e.g., "LCMV-DE")
   * Set link cutoff (default: 0.4)
   * Click "Define Links"
   * Controls which connections to show

Step 2: Customize Appearance
^^^^^^^^^^^^^^^^^^^^^^^^^
1. Colors
   * Choose colors for each cell type
   * Select receptor color
   * Colors help distinguish different cells

2. Link Appearance
   * Link size: Controls connection thickness
   * Enable transparency if needed
   * Adjust text size for labels

3. Layout Options
   * Text position: Inside/Outside/Both
   * Sort mode: Default/Ascending/Descending
   * Gap between sections: 1-10 degrees

Step 3: Generate and Export
^^^^^^^^^^^^^^^^^^^^^^^^
1. Click "Generate Circos Plot"
   * View the plot
   * Check if adjustments needed
   * Regenerate if necessary

2. Export Options
   * Set resolution (DPI)
   * Click "Download Plot"
   * Save as TIFF file

Recommended Settings
------------------

For Clear Visualization
^^^^^^^^^^^^^^^^^^^^^
* Link size: 1.0
* Text size: 0.6
* Gap: 1 degree
* DPI: 300 (minimum for publication)

For Dense Data
^^^^^^^^^^^^
* Enable transparency
* Reduce number of top receptors
* Increase gap between sectors
* Adjust text position to "Outside"

.. tip::
   Start with default settings and adjust based on your needs. If the plot looks crowded, reduce the number of connections shown.

.. note::
   For publication-quality images, use at least 300 DPI resolution.

References
------------------

1. Gu, Z. et al. circlize implements and enhances circular visualization in R. Bioinformatics 30, 2811-2812 (2014).

2. Krzywinski, M. et al. Circos: an Information Aesthetic for Comparative Genomics. Genome Res. 19, 1639-1645 (2009).