====================
Load Dataset
====================

### Overview

In this section, you will learn how to load a single-cell RNA sequencing dataset into the application for analysis. The application supports various data formats and offers several options to configure the loading process according to the dataset's type.

### Supported Data Formats

- **10X Genomics**: `.zip` file containing `barcodes.tsv.gz`, `matrix.mtx.gz`, and `features.tsv.gz`.
- **Seurat Objects**: `.rds` format, which is an R data file.

### Steps to Load a Dataset

1. **Select Dataset Type**: Choose between "snRNA-seq" or "Multiome" based on your dataset.
2. **Upload Data**: Use the "Choose File" button to select your dataset file. Ensure it's a `.zip` file or a `.rds` file.
3. **Configure Options**:
   - For 10X Genomics data, make sure all three files (`barcodes.tsv.gz`, `matrix.mtx.gz`, and `features.tsv.gz`) are included in the `.zip`.
   - For Seurat Objects, ensure the `.rds` file is valid and not corrupted.


.. image:: _static/image_load_data.png
   :alt: Image illustrant le projet
   :width: 50%
   :align: center


.. tip::
   Before uploading, double-check that the dataset file is in the correct format and contains all necessary components. This can prevent errors during loading.

.. warning::
   If the file format is incorrect or missing necessary files, the loading process will fail, and you will receive an error message. Always verify the dataset integrity before uploading.

### Common Issues and Solutions

- **Error: Unsupported file type**: Make sure the file extension is correct (.zip for 10X or .rds for Seurat).
- **Error: File not found**: Check the file path and ensure the file is accessible.
- **Error: Missing files in `.zip`**: Ensure all required files (`barcodes.tsv.gz`, `matrix.mtx.gz`, `features.tsv.gz`) are present in the archive.

.. note::
   It is recommended to back up your original data files before loading them into the application to prevent data loss.
