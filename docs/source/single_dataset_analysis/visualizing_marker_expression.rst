Visualizing Marker Expression
===================================

Overview
--------------------
Visualizing marker gene expression is essential for understanding the biological significance of different cell clusters and their heterogeneity. The application provides multiple visualization options to explore gene expression data effectively.

Available Plot Types
--------------------

Feature Plot
--------------------
- Purpose: Spatial visualization of gene expression
- Features:
  * Expression levels shown on UMAP
  * Color intensity indicates expression level
  * Multiple genes can be shown together
- Options:
  * Min/Max cutoffs for expression
  * Remove axes/legend
  * Show co-expression
  * Color scheme selection

Violin Plot
--------------------
- Purpose: Distribution of expression within clusters
- Features:
  * Shows expression spread per cluster
  * Points represent individual cells
  * Width indicates cell density
- Options:
  * Hide individual points
  * Remove axes/legend
  * Adjust point size

Dot Plot
--------------------
- Purpose: Summary of expression patterns
- Features:
  * Dot size = percentage expressing
  * Color intensity = average expression
  * Multiple genes across clusters
- Options:
  * Cluster ordering
  * Axis rotation
  * Remove axes/legend

Ridge Plot
--------------------
- Purpose: Distribution comparison across clusters
- Features:
  * Layered density plots
  * Clear expression differences
  * Smooth visualization
- Options:
  * Remove axes/legend
  * Adjust plot parameters

How to Visualize Marker Expression
--------------------

1. Select Genes  
Use the dropdown menu to select one or more genes to visualize. You can select multiple genes for comparative visualization in some plot types.

.. image:: ../_static/images/single_dataset_analysis/visualizing_marker_expression_1.png
   :width: 90%
   :align: center

2. Choose Plot Type and Settings
   * Select desired visualization
   * Adjust specific plot parameters
   * Choose display options

3. Generate and Customize Plot
   * Click display button
   * Modify aesthetics
   * Add/remove features

.. image:: ../_static/images/single_dataset_analysis/visualizing_marker_expression.png
   :width: 90%
   :align: center

.. tip::
   * Use Feature Plot for spatial patterns
   * Violin Plot for expression distributions
   * Dot Plot for multi-gene comparisons
   * Ridge Plot for distribution overlays

.. warning::
   * Check expression scales
   * Consider cluster sizes
   * Watch for outliers
   * Validate patterns