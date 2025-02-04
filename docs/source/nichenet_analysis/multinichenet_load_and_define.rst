==========================
MultiNicheNet Analysis
==========================

Overview
--------
MultiNicheNet extends NicheNet to analyze cell-cell communication across multiple experimental conditions, enabling comparison of intercellular signaling between different states or treatments.

Required Files
-------------

Before starting your analysis, prepare these files:

1. **Your Data**
   * Seurat object (.rds) or SingleCellExperiment object (.rds)
   * Must include:
     - Gene expression matrix
     - Cell type annotations
     - Sample/condition labels
     - Quality control metrics

2. **Network Files** 
   
   A. **Ligand-Receptor Network**
      * For Human: `Download Human Network <https://zenodo.org/record/10229222/files/lr_network_human_allInfo_30112033.rds>`_
      * For Mouse: `Download Mouse Network <https://zenodo.org/record/10229222/files/lr_network_mouse_allInfo_30112033.rds>`_
   
   B. **Ligand-Target Matrix**
      * For Human: `Download Human Matrix <https://zenodo.org/record/7074291/files/ligand_target_matrix_nsga2r_final.rds>`_
      * For Mouse: `Download Mouse Matrix <https://zenodo.org/record/7074291/files/ligand_target_matrix_nsga2r_final_mouse.rds>`_

Step-by-Step Analysis
--------------------

1. **Load Your Data**
   * Click "Open Data Loading Menu"
   * Load your Seurat/SingleCellExperiment object
   * Load network files you downloaded
   * Wait for confirmation message

2. **Define Metadata Parameters**
   
   A. **Sample ID**
      * Select column containing sample identifiers
      * Each sample must have unique ID
      * Used to track individual samples
   
   B. **Group ID**
      * Select column with experimental conditions
      * Examples: "treatment", "timepoint", "disease_state"
      * Used for comparisons
   
   C. **Cell Type ID**
      * Select column with cell type labels
      * Must be consistent across samples
      * Used for cell type analysis

3. **Set Up Contrasts**
   * Select groups to compare
   * System generates contrast formula
   * Validates comparison setup
   * Shows formula preview

Important Considerations
----------------------
* Minimum 100 cells per group recommended
* Clean, consistent annotations required
* 16GB RAM minimum recommended
* Multi-core processing supported

### References

1. Browaeys, R., et al. (2020) Nature Methods 17:159-162.
2. MultiNicheNet documentation: github.com/saeyslab/multinichenet
3. Network resources: zenodo.org/7074291