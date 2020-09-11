## Title
The Impact of Random Models on Clustering Similarity
### MetaData
##### Url
http://arxiv.org/abs/1701.06508
##### Type
analysis and improved method

##### Domain
statistics, math, compsci

##### Keywords
clustering, unsupervised



##### Cite
e.g. BibLatex
```LaTex
@article{Gates2017,
abstract = {Clustering is a central approach for unsupervised learning. After clustering is applied, the most fundamental analysis is to quantitatively compare clusterings. Such comparisons are crucial for the evaluation of clustering methods as well as other tasks such as consensus clustering. It is often argued that, in order to establish a baseline, clustering similarity should be assessed in the context of a random ensemble of clusterings. The prevailing assumption for the random clustering ensemble is the permutation model in which the number and sizes of clusters are fixed. However, this assumption does not necessarily hold in practice; for example, multiple runs of K-means clustering returns clusterings with a fixed number of clusters, while the cluster size distribution varies greatly. Here, we derive corrected variants of two clustering similarity measures (the Rand index and Mutual Information) in the context of two random clustering ensembles in which the number and sizes of clusters vary. In addition, we study the impact of one-sided comparisons in the scenario with a reference clustering. The consequences of different random models are illustrated using synthetic examples, handwriting recognition, and gene expression data. We demonstrate that the choice of random model can have a drastic impact on the ranking of similar clustering pairs, and the evaluation of a clustering method with respect to a random baseline; thus, the choice of random clustering model should be carefully justified.},
archivePrefix = {arXiv},
arxivId = {1701.06508},
author = {Gates, Alexander J and Ahn, Yong-Yeol},
eprint = {1701.06508},
file = {:home/bcardoen/Downloads/17-039.pdf:pdf},
keywords = {adjustment for chance,clustering comparison,clustering evaluation,index,normalized mutual information,rand},
mendeley-groups = {Machine learning,SRM},
pages = {1--28},
title = {{The Impact of Random Models on Clustering Similarity}},
url = {http://arxiv.org/abs/1701.06508},
volume = {18},
year = {2017}
}


```
## Content
#### Research Question
How good is the clustering ?
To what baseline do we compare (reference clustering)

#### Contribution
- guidelines for which model to pick when
- improved derivation of NMI and RI

#### Method
##### Clustering metrics:
- compare cluster result to gold standard
- RI, NNI range of [0,1] but do not use full range (1=identity). Values concentrated at 0,1
- compare clustering to random ensemble
  - 1 is identity
  - 0 is expected value of random clustering
  - < 0 similarity is lower than random
- model of random clusterings
- how is random model sampled
- choice is often ignored while critical
- most often used is uniform permutation model (Mperm)
  - Mperm: k-clusters, size of clusters is fixed, assignment is permuted

#### Related Work
Place work in field

#### Data
Describe dataset (for reviews, covered literature)

#### Evaluation
Evaluation method, statistics, ...

#### Conclusion
Succinct summary

#### Notes

#### Extra References
