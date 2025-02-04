==========================
Run and View Results
==========================

Overview
--------
After defining your metadata and contrasts, this section allows you to run the differential expression analysis between your conditions. 

Understanding Key Parameters
--------------------------

Before running the analysis, few parameters need to be understood:

**Expression Thresholds**
   * "Minimum sample proportion" (0.50): Percentage of samples where a gene should be expressed
   * "Expression fraction cutoff" (0.05): Percentage of cells that should express a gene
   * These values help filter out noise while keeping relevant signals

**Statistical Controls**
   * "LogFC threshold" (0.50): How much change is considered significant
   * "P-value threshold" (0.05): Statistical significance level
   * You can enable empirical p-values and multiple testing correction for more stringent analysis

Running Your Analysis
-------------------

1. **First Step: Calculate Expression**
   * Click "Calculate Abundance & Expression"
   * This step prepares your data
   * Wait for completion before next step

2. **Second Step: Run Analysis**
   * Click "Run Expression & DE Analysis"
   * Analysis will process using your settings
   * Results appear in P-value distribution plot

Interpreting Results
------------------
The P-value distribution plot shows how significant your results are. A good analysis typically shows:
   * A peak near zero (significant changes)
   * A flat distribution elsewhere
   * You can download this plot for publication

.. tip::
   Start with the default parameters. Only adjust if you have specific reasons or if results don't match expectations.
