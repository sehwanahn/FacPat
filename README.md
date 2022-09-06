<!--
# FacPat

Factors-specific pattern mining from large-scale drug-induced gene expression profiles

SeHwan Ahn*, JuHan Kim*

# Abstract
Identifying the relationships among drugs, diseases, and genes from large-scale drug-induced gene expression profiles is important in drug discovery. Significant biological features can be identified from multivariate large-scale drug-induced gene expression profiles. However, it is necessary to develop new approaches and methods that can efficiently identify important features in a large-scale multivariate dataset.

We present FacPat, which identifies the optimal factor(s)-specific patterns that explain the expression profiles of drug-induced differentially expressed signatures. We mined the optimal factor-specific patterns using a genetic algorithm based on the pattern distance. Because we scored the pattern distance for each gene, we applied a Benjamini Hochberg correction to control the false discovery rate. Finally, we discovered significant and directly interpretable factor-specific patterns consisting of 480 genes, 7 chemical compounds, and 38 human cell lines.
-->

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
This project is licensed under the Seoul National University Biomedical Informatics (SNUBI), Division of Biomedical Informatics, Seoul National University College of Medicine, Seoul, Republic of Korea.   
This source code and data can be used only for NON COMMERCIAL purposes.
