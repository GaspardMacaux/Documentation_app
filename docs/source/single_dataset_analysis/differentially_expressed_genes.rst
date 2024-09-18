===========================================
Differentially Expressed Genes (DEGs)
===========================================

### Overview

Identifying **Differentially Expressed Genes (DEGs)** is essential for understanding the biological differences between cell clusters or experimental conditions. DEGs are genes that show statistically significant differences in expression between two groups, such as different clusters of cells. This can help reveal important markers that distinguish cell types or states, or highlight genes that are responding to specific experimental conditions.

In this application, DEGs are identified by comparing the expression levels of genes across different clusters of cells.

### Key Concepts

- **Log Fold Change (logFC)**:  
  Log fold change measures the difference in expression levels between two groups (e.g., clusters) on a logarithmic scale. A higher logFC indicates a more substantial difference in expression. For example, a logFC of 1 means that a gene is expressed two times more in one cluster compared to another. You can set a threshold to control the minimum logFC required for a gene to be considered differentially expressed.

- **Percentage Threshold**:  
  This parameter controls the minimum percentage of cells within a cluster that must express the gene for it to be considered in the analysis. This prevents genes that are expressed in only a few cells from being falsely classified as DEGs.

- **Statistical Significance (p-value and adjusted p-value)**:  
  Once the DEGs are identified, they are assessed for statistical significance using p-values. The p-values are also adjusted (e.g., using the Bonferroni or Benjamini-Hochberg correction) to account for multiple testing.

### How to Identify DEGs

1. **Select Parameters**:  
   To identify DEGs, you need to set the following parameters:
   - **Log Fold Change Threshold**: The minimum log fold change to consider a gene differentially expressed. By default, this is set to 0.25, meaning that only genes with at least a 1.19x difference in expression will be considered.
   - **Percentage Threshold**: The minimum percentage of cells in each cluster that must express the gene for it to be included in the analysis. For example, a threshold of 0.1 (10%) means the gene must be expressed in at least 10% of the cells in one cluster.

2. **Run DEG Analysis**:  
   After selecting the parameters, click **"Find DEGs"** to perform the differential expression analysis. The application will identify genes that are significantly different between the selected clusters based on the provided thresholds.

   .. image:: ../_static/images/single_dataset_analysis/differentially_expressed_genes.png
      :width: 90%
      :align: center

3. **Download Results**:  
   After the analysis, you can download the identified DEGs as a CSV file. The DEGs are displayed in a table where each gene's log fold change, p-value, and adjusted p-value are shown.

   - **Download DEGs**: Click **Download differentially expressed genes** to download the results in CSV format.
   - **Save Seurat Object**: Save the entire Seurat object, by clicking **Save Seurat Object**.

4. *Interacting with DEG Results:**

- The `gene` column in the DEGs table is interactive. Clicking on a gene name will attempt to open a new tab or window in your browser, directing you to the Protein Atlas page for that gene.
- If clicking the gene name does not open the link, ensure that pop-ups are enabled for this site in your web browser.

.. tip::
   Make sure your web browser allows pop-ups from this site to enable direct navigation to external gene resources.

**Technical Details:**

The application uses the Protein Atlas API to search for the Ensembl ID of the selected gene and directs you to the corresponding page.

.. tip::
   Start with a **log fold change threshold** of 0.25 and a **percentage threshold** of 10% (0.1) to get a balanced set of DEGs. If you find too many DEGs, try increasing the thresholds.

.. warning::
   Setting thresholds that are too low may result in many false positives (genes that appear to be differentially expressed but are not biologically significant), while setting thresholds that are too high may cause important DEGs to be missed. Adjust these thresholds based on your dataset’s size and characteristics.


### Common Issues

- **No DEGs Found**:  
   If no DEGs are found, consider lowering the **log fold change threshold** or increasing the **percentage threshold**. A lower log fold change will capture more subtle changes in gene expression, and increasing the percentage threshold ensures that only genes expressed in more cells are considered.

- **Too Many DEGs**:  
   If you find too many DEGs, try increasing the log fold change threshold or decreasing the percentage threshold. This will help you focus on genes with stronger expression differences and filter out those that may not be biologically relevant.
