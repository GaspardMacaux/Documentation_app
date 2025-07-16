# Introduction

Welcome to our Single-Cell and Single-Nucleus RNA sequencing (scRNA-seq and snRNA-seq) data analysis application. The data you will be exploring are produced using 10x Genomics technology, a cutting-edge method for genome-wide profiling of single cells and nuclei. This allows us to analyze gene expression at the level of a single cell or nucleus, offering unprecedented resolution for understanding biological mechanisms. This application utilizes the Seurat, CellCha, Monocle and Nichenet libraries. Seurat is a popular R tool for scRNA-seq and snRNA-seq analysis. It offers a suite of tools for quality, analysis, exploration, and visualization of such data. Monocle provides a trajectory analysis that helps us to analyse the fate of cells.

This application allows anyone who is not familiar with computer code to use many of the functions of these libraries, thereby democratising the analysis of this type of data.

We hope you will find this application useful and informative. Happy exploring!

![](/_static/images/introduction/pipeline.png)

```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Welcome

introduction_app/introduction
introduction_app/installation
```

```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Single Dataset Analysis

single_dataset_analysis/load_dataset
single_dataset_analysis/data_cleanup
single_dataset_analysis/dimentional_reduction
single_dataset_analysis/clustering
single_dataset_analysis/doublet_finder
single_dataset_analysis/visualizing_marker_expression
single_dataset_analysis/heatmaps
single_dataset_analysis/assigning_cell_identity
single_dataset_analysis/cluster_biomarkers
single_dataset_analysis/subset
```

```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Multiple Datasets Analysis

multiple_datasets_analysis/load_datasets_merge
multiple_datasets_analysis/clustering_merge
multiple_datasets_analysis/genes_expressions_merge
multiple_datasets_analysis/heatmap_merge
multiple_datasets_analysis/assigning_cell_identity_merge
multiple_datasets_analysis/biomarkers_merge
multiple_datasets_analysis/subset_merge
```

```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Cell Chat

cellchat_analysis/cellchat_load
cellchat_analysis/cellchat_ligandreceptor
cellchat_analysis/cellchat_circleplot
```

```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Monocle

trajectory_analysis/trajectory_analysis
trajectory_analysis/genes_pseudotime
```


```{toctree}
:maxdepth: 1
:titlesonly:
:caption: Acknowledgment & Licence

acknowledgment
```