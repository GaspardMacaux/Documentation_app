Differentially expressed genes 
==============================

Overview
--------------------
Identifying differentially expressed genes (DEGs) is essential for understanding what makes cell populations unique. This analysis reveals genes that are significantly more or less active in specific cell types or conditions, providing insights into cellular functions and identities.

Concept of Differential Expression
--------------------
Differential expression analysis compares gene expression levels between groups of cells to find significant differences. These differences help us understand:
- What makes each cell type unique
- How cells respond to different conditions
- Which genes might serve as markers for specific cell populations

.. image:: ../_static/images/differentialy_expressed_1_merge.png
   :width: 90%
   :align: center

Key Steps in Analysis
--------------------

Statistical Testing
--------------------
The analysis uses statistical tests to identify significant differences in gene expression between groups:
- Compares expression levels between clusters
- Calculates significance (p-values)
- Identifies consistently different genes

.. image:: ../_static/images/differentialy_expressed_1_merge.png
   :width: 90%
   :align: center

Parameter Selection
--------------------

Log2FC Threshold
--------------------
- What it is: Minimum difference in expression between groups
- Default value: 0.25
- How to adjust:
  * Higher values (>0.5): Find strongly different genes
  * Lower values (<0.25): Include subtle differences
- Impact: Controls the magnitude of difference required

Percentage Threshold
--------------------
- What it is: Minimum percentage of cells expressing the gene
- Default value: 0.01 (1%)
- How to adjust:
  * Higher values: Focus on commonly expressed genes
  * Lower values: Include rare gene expression
- Impact: Filters out genes expressed in too few cells

Display Settings
--------------------
- What it is: How many top genes to show in results
- Default: 10 genes
- Range: 1 to 2000
- Impact: Controls the length of your results list

Running the Analysis
--------------------

Step-by-Step Process
--------------------
1. Set your parameters:
   - Adjust Log2FC threshold
   - Set percentage threshold
   - Choose number of genes to display
2. Start the Analysis:
   - Click "Differentially expressed genes"
   - Wait for computation to complete
   - Review results in the generated tables
3. Save Your Results:
   - Download full results as CSV
   - Save updated Seurat object for future analysis

Interpreting Results
--------------------

Results Table Content
--------------------
- Gene names
- Average expression in each group
- Log fold change values
- Statistical significance (p-values)
- Percentage of cells expressing each gene

Key Metrics
--------------------
1. Log Fold Change
   - Positive values: Higher in target group
   - Negative values: Lower in target group
   - Magnitude indicates strength of difference

2. P-values
   - Lower values indicate stronger significance
   - Generally look for p < 0.05
   - Consider adjusting for multiple testing

3. Expression Percentages
   - Higher percentages suggest more reliable markers
   - Low percentages might indicate rare cell types

Practical Tips
--------------------

For General Analysis
--------------------
- Start with default parameters
- Adjust based on your specific needs
- Consider biological relevance, not just statistics

For Marker Discovery
--------------------
- Use stricter thresholds (higher Log2FC)
- Look for high percentage expression
- Focus on genes with clear biological roles

For Exploratory Analysis
--------------------
- Use more permissive thresholds
- Look at more genes (increase display number)
- Consider patterns across multiple genes