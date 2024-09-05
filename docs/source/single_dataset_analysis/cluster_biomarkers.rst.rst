================================
Cluster Biomarkers
================================

### Overview

Cluster biomarkers are genes that are uniquely or highly expressed in specific clusters, providing insights into their biological identity and function.

### Steps to Identify Cluster Biomarkers

1. **Select Cluster for Analysis**: Choose a cluster to identify its biomarkers.
2. **Set Biomarker Parameters**: Adjust the log fold change and percentage thresholds for biomarker identification.
3. **Run Biomarker Analysis**: Click "Find Biomarkers" to perform the analysis.

.. tip::
   Biomarkers with a high log fold change and expression in a significant percentage of cells within a cluster are often more robust and reliable.

.. warning::
   Selecting biomarkers based solely on statistical significance may lead to false positives. Consider biological relevance as well.

### Visualizing Cluster Biomarkers

- **Feature Plot**: Visualize the expression of identified biomarkers across clusters.
- **Heatmap**: Display the expression levels of biomarkers across all clusters for comparison.

### Common Issues

- **No biomarkers identified**: Adjust the thresholds or consider alternative methods for biomarker detection.
- **Too many biomarkers**: Increase the stringency of thresholds to focus on more specific biomarkers.
