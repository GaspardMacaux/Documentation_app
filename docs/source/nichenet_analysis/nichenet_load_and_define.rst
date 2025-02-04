==========================
NicheNet Analysis
==========================

Overview
--------
NicheNet analyzes cell-cell communication by predicting which ligands from sender cells influence gene expression in receiver cells.

Required Files
-------------

Before starting, you need to download several files:

1. **Your Data**
   * A Seurat object (.rds) containing your analyzed single-cell data
   * Must include cell type annotations and experimental conditions

2. **Network Files** 
   
   A. Ligand-Receptor Network:
      * Download for your species:
      * `Human Network <https://zenodo.org/record/10229222>`_
      * `Mouse Network <https://zenodo.org/record/10229222/files/lr_network_mouse_allInfo_30112033.rds>`_
   
   B. Ligand-Target Matrix:
      * Download from: `Ligand-Target Matrix <https://zenodo.org/record/7074291/files/ligand_target_matrix_nsga2r_final.rds>`_
   
   C. Weighted Networks:
      * Download from: `Weighted Networks <https://zenodo.org/record/7074291>`_

Loading Your Data
---------------

1. **Open Data Loading Menu**
   * Click the "Open Data Loading Menu" button
   * Click "Choose File" to load your Seurat object
   * Upload the three network files you downloaded
   * Wait for confirmation of successful loading

Setting Up Analysis
-----------------

1. **Define Cell Populations**
   * Select Cell Identity Column containing your cell type annotations
   * Choose Sender cell types (cells producing signals)
   * Choose Receiver cell types (cells responding to signals)

2. **Configure Conditions**
   * Select Condition Column (e.g., "treatment", "timepoint")
   * Choose Condition of Interest (experimental group)
   * Choose Reference Condition (control group)

3. **Set Analysis Parameters**
   * Expression Percentage Threshold: 
     - Default: 0.05
     - Range: 0.01-1.0
     - Lower values include rare events
   * Number of Top Ligands:
     - Default: 50
     - Range: 1-200
     - Higher numbers include more interactions

Running Analysis
--------------
* Click "Run NicheNet Analysis"
* Analysis progress will be displayed
* Results will appear in the Results tab

.. note::
   Make sure to download all required network files before starting. The analysis cannot proceed without them.

.. tip::
   Start with default parameters for your first analysis, then adjust based on results.

References
----------

1. Browaeys, R., Saelens, W. & Saeys, Y. NicheNet: modeling intercellular communication by linking ligands to target genes. Nat Methods 17, 159–162 (2020). https://doi.org/10.1038/s41592-019-0667-5

2. https://github.com/saeyslab/nichenetr

3. Network Resources:
   - Human/Mouse Networks: https://doi.org/10.5281/zenodo.7074291
   - Expression Data: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE144357
   - Code Repository: https://github.com/saeyslab/nichenetr
