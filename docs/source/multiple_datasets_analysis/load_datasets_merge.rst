==========================
Load Datasets
==========================

### Overview

In this section, you will learn how to load multiple datasets into a unified analysis environment. Integrating datasets is crucial when dealing with single-cell RNA sequencing data from different sources or conditions. It allows you to perform a comprehensive analysis that considers all datasets as a single entity, enabling direct comparisons and joint analysis.

### Concept of Data Integration

Data integration in the context of single-cell RNA sequencing involves combining multiple datasets (e.g., from different experiments or conditions) into a single cohesive dataset. This process is necessary to:

- Reduce batch effects and technical variations that may arise from different sequencing runs.
- Increase the statistical power by pooling cells from multiple datasets.
- Enable a unified analysis across different conditions or experimental setups.

### Key Steps in the Integration Process

1. **Data Loading**:  
   The initial step involves loading Seurat objects or 10X data files, which are standard formats for single-cell RNA sequencing data. This step converts raw data into a format that can be processed and analyzed.

2. **Data Cleaning and Preparation**:  
   After loading, the data is cleaned to remove low-quality cells or genes that might introduce noise into the analysis.

3. **Normalization and Scaling**:  
   The datasets are normalized to account for sequencing depth and scaled to ensure that highly variable genes are prioritized in the downstream analysis.

4. **Integration**:  
   This step involves finding shared features (anchor points) across datasets and aligning them into a common space. The result is a single integrated dataset that can be analyzed as a whole.

.. image:: ../_static/images/multiple_datasets_analysis/load_datasets_merge.png
   :width: 90%
   :align: center

.. tip::  
   Use Seurat objects saved in `.rds` format for faster loading and processing. Ensure that the data is properly formatted and pre-processed before integration to minimize errors.

.. warning::  
   Improperly formatted datasets or those from different species may cause integration errors or produce misleading results. Always check dataset compatibility before integrating.

### Instructions for Loading Datasets

1. **Prepare Your Datasets**:  
   - Compress the three 10X files (`barcodes.tsv.gz`, `matrix.mtx.gz`, and `features.tsv.gz`) into a single `.zip` file for each dataset.
   - Alternatively, prepare your data in `.rds` format if you are using Seurat objects.

2. **Set the Number of Datasets**:  
   Enter the number of datasets you wish to upload in the "Enter number of datasets to upload" field.

3. **Select Species**:  
   Choose the species of the datasets you are loading (`Mouse` or `Human`). This affects how mitochondrial genes are identified during data processing.

4. **Upload the Datasets**:  
   - For each dataset, select the data type (`snRNA-seq`, `Multiome`, or `Seurat Object`) and upload the corresponding file using the provided interface.
   - If loading a Seurat object, you can directly upload an `.rds` file.

5. **Integration**:  
   Once all datasets are uploaded, click the "Integrate" button to combine them into a single integrated dataset.

### Metadata Management

- After integration, you can add custom metadata fields:
   - Click "Add Metadata Field" to specify new metadata fields for the integrated dataset.
   - Enter the field names and values for each dataset and click "Add Metadata" to append this information to the integrated dataset.

### Troubleshooting

- **Error During Integration**:  
   Ensure that at least two datasets are uploaded and that the files are correctly formatted. If an error occurs, check the log for details.

By following these steps, you can effectively load and integrate multiple single-cell RNA sequencing datasets, enabling comprehensive and unified analysis.
