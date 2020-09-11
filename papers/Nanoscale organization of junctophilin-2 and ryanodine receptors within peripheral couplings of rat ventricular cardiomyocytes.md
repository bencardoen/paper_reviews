## Title
Nanoscale Organization of Junctophilin-2 and Ryanodine Receptors within Peripheral Couplings of Rat Ventricular Cardiomyocytes
### MetaData
##### Url
http://dx.doi.org/10.1016/j.bpj.2012.01.034
##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Jayasinghe2012,
abstract = {The peripheral distributions of the cardiac ryanodine receptor (RyR) and a junctional protein, junctophilin-2 (JPH2), were examined using single fluorophore localization-based super-resolution microscopy in rat ventricular myocytes. JPH2 was strongly associated with RyR clusters. Estimates of the colocalizing fraction of JPH labeling with RyR was ∼90{\%} within 30 nm of RyR clusters. This is comparable to fractions estimated from confocal data (∼87{\%}). Similarly, most RyRs were associated with JPH2 labeling in super-resolution images (∼81{\%} within 30 nm of JPH2 clusters). The shape of associated RyR clusters and JPH2 clusters were very similar, but not identical, suggesting that JPH2 is dispersed throughout RyR clusters and that the packing of JPH2 into junctions and the assembly of RyR clusters are tightly linked. {\textcopyright} 2012 Biophysical Society.},
author = {Jayasinghe, Isuru D. and Baddeley, David and Kong, Cherrie H.T. and Wehrens, Xander H.T. and Cannell, Mark B. and Soeller, Christian},
doi = {10.1016/j.bpj.2012.01.034},
file = {:home/bcardoen/Downloads/main.pdf:pdf},
issn = {00063495},
journal = {Biophysical Journal},
mendeley-groups = {doublelabelling,SRM},
number = {5},
pages = {L19--L21},
publisher = {Biophysical Society},
title = {{Nanoscale organization of junctophilin-2 and ryanodine receptors within peripheral couplings of rat ventricular cardiomyocytes}},
url = {http://dx.doi.org/10.1016/j.bpj.2012.01.034},
volume = {102},
year = {2012}
}


```
## Content
#### Research Question
- Colocalization of 2 signalling proteins in rat heart muscle

#### Contribution
Summarized contribution(s)

#### Method
-Colocalization is lower in SR than it is in confocal
-adding a 30nm band increases overlap
-this is a result from using SR to expect overlap (where physically it cannot exit)
-distance maps of cluster to cluster
-distance histogram w.r.t. nearest cluster (2D)
-compare angular alignment of clusters
 - if 2 clusters overlap, compare angular alignment, do this for all pairs
 - then compare with randomly (not overlapping) clusters
###### Analysis technique details
- location binned in 5nm pixel grid --> event data to density map using Visualization of Localization Microscopy Data (Delaunay)
- use a 30nm band reflective of the resolution of the system as determining the precision
- binarize density by connecting everything within 30nm (precision (assumed))
- distances in cluster are negative, outside are positive
- Mander's coefficient for fractional overlap
- Rotational alignment (find the rotation needed for alignment, then compare with random)
- Showed the expected correlation is +- .7 in identical structure case, not 1

#### Related Work

#### Data
2D SMLM of protein receptors labelled with dual color, 2-stage antibody

#### Evaluation

#### Conclusion
Colocalization by cluster distance analysis with a uncertainty boundary

#### Notes

#### Extra References
