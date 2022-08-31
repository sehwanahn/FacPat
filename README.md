# FacPat

Factor-specific pattern mining from a large-scale drug-induced gene expression profile

SeHwan Ahn*, JuHan Kim*

# Abstract
Identifying relationships among drugs, diseases, and genes from large-scale drug-induced gene expression profiles is important in drug discovery. The significant biological features can be identified from multi-variate large-scale drug-induced gene expression profiles. However, it is necessary to develop new ap-proaches and methods that can efficiently identify important features on a large-scale multivariate dataset.

We present FacPat, which identifies the optimal factor(s)-specific patterns explaining the ex-pression profiles of differentially expressed signatures induced by drugs. We mined the optimal factor-specific patterns using a genetic algorithm based on the pattern distance. To deal with multiple testing problems, we generated the distribution of the pattern distances by shuffling sample labels of expression profiles. Then, we determined the p-value from the distribution of the pattern distances and converted it to a q-value with Benjamini and Hochberg method. Finally, we discovered significant and directly inter-pretable factor-specific patterns consisting of 480 genes, 7 chemical compounds, and 38 human cell lines.

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
