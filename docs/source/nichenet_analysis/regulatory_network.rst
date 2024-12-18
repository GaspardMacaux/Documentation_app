==========================
Regulatory Network
==========================

Overview
--------
The Regulatory Network visualizes interactions between cell populations, helping you understand communication patterns in your data.

Creating Your Network
------------------

1. **Basic Settings**
  * Set number of top interactions (default: 50)
  * Enable correlation filtering if needed
  * Click "Generate Network"

2. **Visual Customization**
  * Select specific sender cells to highlight
  * Choose custom colors for selected senders
  * Default color is pink

3. **Export Options**
  * Set resolution (300 DPI recommended)
  * Download network as high-quality plot
  * Publication-ready format

Understanding the Visualization 
---------------------------
The network shows:
  * Sender cells as colored nodes
  * Receptor cells as targets
  * Connection strength by line thickness
  * Interaction patterns between populations

Best Practices
------------
* Start with fewer interactions (~50) to avoid clutter
* Use correlation filtering for more confident interactions
* Highlight key senders with distinct colors
* Export in high resolution for publication

.. tip::
  If network looks too dense, reduce number of interactions and try correlation filtering.

.. note::
  Use 300+ DPI resolution for publication-quality figures.

References
----------

1. `MultiNicheNet Paper <https://doi.org/10.1101/2023.06.13.544751>`_

2.`Network Analysis Examples <https://github.com/saeyslab/multinichenetr/vignettes>`_

