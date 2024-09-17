===============================
Cluster Biomarkers
===============================

### Overview

Cluster biomarkers are genes that are uniquely or highly expressed in specific clusters, providing insights into their biological identity and function. This section allows you to identify such biomarkers by comparing the expression levels between clusters.

### Steps to Identify Cluster Biomarkers

1. **Select Cluster for Analysis**:  
   Choose a cluster to identify its biomarkers. This can be done in two ways:
   - **Compare one cluster with all others**: Identify biomarkers that are uniquely expressed in one cluster compared to all other clusters.
   - **Compare one cluster with another cluster**: Identify differentially expressed genes between two specific clusters.

2. **Set Biomarker Parameters**:  
   Adjust the parameters to define the criteria for biomarker identification:
   - **Log2 Fold Change threshold**: Set the minimum log fold change to consider a gene as differentially expressed. Higher values will filter for genes with greater differences in expression between clusters.
   - **Minimum percentage threshold**: Define the minimum percentage of cells within the cluster that must express the gene for it to be considered. This helps to ensure that the identified biomarkers are expressed in a significant portion of the cluster.

3. **Run Biomarker Analysis**:  
   - Click "Start analysis" under the relevant section to perform the biomarker identification. 
   - If comparing one cluster with all others, select the cluster of interest and set the parameters.
   - If comparing two clusters, select both clusters and adjust the parameters accordingly.

.. image:: ../_static/images/single_dataset_analysis/cluster_biomarkers.png
   :width: 90%
   :align: center

.. tip::  
   Biomarkers with a high log fold change and expression in a significant percentage of cells within a cluster are often more robust and reliable.

.. warning::  
   Selecting biomarkers based solely on statistical significance may lead to false positives. Consider the biological relevance and the context of your analysis.

### Output and Download Options

- **Biomarker Tables**:  
  After running the analysis:
  - The table displaying the differentially expressed genes for the selected clusters will be shown.
  - Click "Download table (csv)" to export the identified biomarkers and their statistics.

### Common Issues

- **No biomarkers identified**:  
   If no biomarkers are found, consider lowering the `Log2 Fold Change threshold` or the `Minimum percentage threshold`. This adjustment can make the criteria less stringent and may reveal more potential biomarkers.

- **Too many biomarkers**:  
   If the results include too many biomarkers, increase the thresholds to focus on genes with stronger differential expression or a higher percentage of expression within the cluster.

### Troubleshooting

- **Error During Analysis**:  
   Ensure that the clusters selected are distinct and that input parameters such as `Log2 Fold Change threshold` and `Minimum percentage threshold` are appropriately set. Verify that the dataset is correctly formatted and loaded.
