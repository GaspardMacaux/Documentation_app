# Genes Pseudotime

## Overview
The "Genes Pseudotime" tab focuses on identifying differentially expressed genes along the inferred trajectory, allowing for the exploration of gene dynamics over pseudo-time. This analysis can reveal genes that play crucial roles at different stages of a biological process.

## Understanding the Analysis
Genes Pseudotime Analysis is used to identify and visualize genes whose expression levels change along the trajectory. These changes provide insights into the molecular mechanisms driving the biological process represented by the trajectory.

## Key Analysis Steps

### Differential Expression Analysis
- After ordering cells in pseudotime, differential expression analysis identifies genes that vary significantly
- The graph_test function identifies key drivers of the biological process
- Results highlight genes changing along the trajectory

![](../_static/images/trajectory_analysis/genes_pseudotime_1.png)

### Gene Dynamics Visualization
- Visualize selected genes along trajectory
- Use plot_cells function to show expression patterns
- Track changes across pseudotime

![](../_static/images/trajectory_analysis/genes_pseudotime_2.png)

### Gene Module Analysis
- Identify groups of co-expressed genes
- Use find_gene_modules function
- Explore coordinated expression patterns

## Using the Interface

### Running the Analysis
1. **Calculate Differential Genes**
   - Click "Run Differential Gene Test"
   - Compute expression changes
   - Review results table
2. **Visualize Gene Trajectories**
   - Select genes from picker
   - Click "Visualize Gene Trajectory"
   - Examine expression patterns
3. **Module Analysis**
   - Perform optional module analysis
   - Identify gene groups
   - Visualize module dynamics
4. **Path Analysis**
   - Choose specific genes
   - Select cell types
   - View dynamics along path

> **Tip:**
> Select genes with significant q-values and fold changes to focus on the most impactful genes in the trajectory.

> **Warning:**
> Ensure that the trajectory and pseudotime ordering are biologically meaningful before interpreting gene expression changes.