# Load Datasets

## Overview
In this section, you will learn how to load multiple datasets into a unified analysis environment. Integrating datasets is crucial when dealing with single-cell RNA sequencing data from different sources or conditions. It allows you to perform a comprehensive analysis that considers all datasets as a single entity, enabling direct comparisons and joint analysis.

## Concept of Data Integration
Data integration in the context of single-cell RNA sequencing involves combining multiple datasets (e.g., from different experiments or conditions) into a single cohesive dataset. This process is necessary to:
- Reduce batch effects and technical variations that may arise from different sequencing runs
- Increase the statistical power by pooling cells from multiple datasets
- Enable a unified analysis across different conditions or experimental setups

![](../_static/images/multiple_datasets_analysis/load_datasets_merge.png)

## Data Loading Options

### Option 1: Multiple Raw Datasets
This option is ideal when you have multiple datasets that need to be integrated for comparative analysis.

**Requirements:**
- For each dataset:
  - Raw 10X Genomics data files:
    - barcodes.tsv.gz
    - matrix.mtx.gz
    - features.tsv.gz
  - Files must be compressed into a single ZIP file per dataset
- Alternative format:
  - Individual Seurat objects saved as .rds files
- You can mix both formats during upload

**Loading Process:**
1. Click the "Load Datasets" button in the "Load Multiple Raw Datasets" tab
2. In the modal dialog:
   - Select the number of datasets to upload
   - For each dataset:
     - Choose the data type (snRNA-seq or Multiome)
     - Upload the corresponding ZIP file or .rds file
   - Click "Proceed" to start the integration process

### Option 2: Pre-integrated Object
Use this option when you have a previously integrated Seurat object.

**Requirements:**
- Single .rds file containing an integrated Seurat object
- Object should contain metadata identifying original datasets

**Loading Process:**
1. Navigate to the "Load Pre-integrated Object" tab
2. Use the file browser to select your .rds file
3. Wait for the loading process to complete

## Metadata Management

### Adding Custom Metadata
After loading your data, you can enhance it with additional metadata:
1. Click "Add New Metadata Field"
2. For each field:
   - Enter the field name
   - Provide values for each dataset
3. Click "Save Metadata" to apply changes

### Best Practices for Metadata
- Use consistent naming conventions
- Avoid special characters in field names
- Keep metadata descriptions concise but informative
- Document any specific conditions or treatments

## Additional Resources
- [10X Genomics Documentation](https://support.10xgenomics.com/)
- [Seurat Integration Tutorial](https://satijalab.org/seurat/articles/integration_introduction.html)
- [System Requirements Guide](https://support.10xgenomics.com/single-cell-gene-expression/software/overview/system-requirements)