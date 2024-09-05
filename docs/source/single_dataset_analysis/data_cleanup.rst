==============================
Data Cleanup & Variable Features
==============================

### Overview

Data cleanup is a crucial step in the preprocessing of single-cell RNA sequencing data. It involves filtering out low-quality cells and normalizing the data to prepare it for downstream analysis.

### Steps for Data Cleanup

1. **Set Quality Thresholds**:
   - **Unique Genes Detected**: Adjust the range slider to filter cells based on the number of unique genes detected.
   - **Mitochondrial Content**: Set a maximum percentage for mitochondrial gene content to exclude low-quality cells.
   
2. **Apply Quality Filters**: Click "Apply QC Filters" to remove cells that do not meet the quality criteria.

3. **Normalize Data**: Normalize the dataset to scale the expression levels across cells.

.. tip::
   For scRNA-seq data, a mitochondrial content below 5% is typically considered acceptable to avoid dead or dying cells.

.. warning::
   Overly strict quality filters can lead to the exclusion of too many cells, potentially losing important biological information. Adjust thresholds carefully.

### Variable Features Selection

Selecting variable features is essential for downstream analysis like clustering and dimensional reduction.

1. **Set Number of Variable Features**: Choose the number of highly variable genes to use in the analysis.
2. **Visualize Variable Features**: Use the plots provided to assess the variability and quality of the selected genes.

.. tip::
   A common choice is to select 2000 variable features, but this can be adjusted depending on the dataset size and complexity.

### Troubleshooting

- **No cells pass the filter**: This might indicate that the quality thresholds are too strict. Try lowering the thresholds and applying the filters again.
- **High mitochondrial content**: This can indicate poor sample quality. Consider revising your data preparation protocol.
