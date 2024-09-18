==========================
Cluster Biomarkers
==========================

Identifying cluster-specific biomarkers is essential for distinguishing between different cell types or states within integrated datasets. Biomarkers are genes that are uniquely or highly expressed in a particular cluster, serving as molecular signatures for those clusters.

### Understanding Biomarkers

Biomarkers are characteristic genes whose expression levels are indicative of specific biological states or cell types. In the context of clustering, biomarkers help:

- Differentiate between clusters by their unique gene expression profiles.
- Understand the functional properties of different cell populations.
- Identify potential targets for therapeutic intervention or further study.

### How to Identify and Use Cluster Biomarkers

1. **Biomarker Discovery**:  
   Use differential expression analysis to find genes that are significantly upregulated in a cluster compared to others. This can be done through the interface by selecting clusters and applying the analysis tools.

2. **Comparison Tools**:  
   - **Compare One Cluster with All Others**: Select a cluster to find biomarkers by comparing its gene expression against all other clusters. Adjust the Log2 Fold Change and percentage thresholds to refine the analysis.
   - **Compare Two Clusters**: Choose two clusters for direct comparison to identify differentially expressed genes between them.
   - **Cross-Dataset Cluster Comparison**: Select clusters from two different datasets to compare their gene expression profiles, which is useful for validating findings across different conditions or experimental setups.

3. **Visualization**:  
   Use visualization tools like UMAP plots to display the spatial distribution of biomarkers across clusters.

.. image:: ../_static/images/multiple_datasets_analysis/biomarkers_merge.png
   :width: 90%
   :align: center

### Interface Usage

1. **UMAP Plot Filtering**:  
   - Visualize the clusters in the UMAP plot and filter based on specific datasets or parameters.
   - Download the filtered UMAP plot for documentation or presentation purposes.

2. **Biomarker Analysis**:  
   - Select a cluster for comparison and click "Start analysis" to identify differentially expressed genes.
   - Adjust the Log2 Fold Change threshold and percentage threshold to filter the biomarkers.
   - Download the list of differentially expressed genes for further analysis.

3. **Cluster Comparison**:  
   - Compare two clusters or clusters across datasets by selecting them from the UI and running the analysis.
   - Download the results for each comparison to facilitate downstream analyses.

4. **Generate Cluster Table**:  
   - Generate and view a table providing an overview of clusters with their assigned identities and biomarkers.
