# FacPat

[Factor-specific generative pattern from large-scale drug-induced gene expression profile](https://www.nature.com/articles/s41598-023-33061-x) 

SeHwan Ahn, JuHan Kim<sup>*</sup>  
Scientific Reports 13, 6339 (2023)

# Abstract
Drug discovery is a complex and interdisciplinary field that requires the identification of potential drug targets for specific diseases. In this study, we present FacPat, a novel approach that identifies the optimal factor-specific pattern explaining the drug-induced gene expression profile. FacPat uses a genetic algorithm based on pattern distance to mine the optimal factor-specific pattern for each gene in the LINCS L1000 dataset. We applied Benjamini–Hochberg correction to control the false discovery rate and identified significant and interpretable factor-specific patterns consisting of 480 genes, 7 chemical compounds, and 38 human cell lines. Using our approach, we identified genes that show context-specific effects related to chemical compounds and/or human cell lines. Furthermore, we performed functional enrichment analysis to characterize biological features. We demonstrate that FacPat can be used to reveal novel relationships among drugs, diseases, and genes.

# Overview of FacPat

![FacPat](https://user-images.githubusercontent.com/111483980/187581224-7d117df9-2a65-40d2-a54d-8cb075170eb7.png)


# Requirements
~~~shell
pip install numpy
pip install pandas
~~~

# Usage
~~~shell
usage: FacPat.py [-h] -i INPUT [t THRESHOLD] -o OUTPUT

optional arguments:
  -h, --help    show this help message and exit
  -i INPUT      Input file (tab-delimited)
  -t THRESHOLD  Absolute threshold of Z-score to make binary (default : |2|)
  -o OUTPUT     Output filename prefix (default : output.txt)
~~~

# LICENCE
This project is licensed under the Seoul National University Biomedical Informatics (SNUBI), Department of Biomdeical Sciences, Seoul National University College of Medicine, Seoul, Republic of Korea.   
This source code and data can be used only for NON COMMERCIAL purposes.
