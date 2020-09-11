## Title
Stochastic optical reconstruction microscopy–based relative localization analysis (STORM-RLA) for quantitative nanoscale assessment of spatial protein organization
### MetaData
##### Url

##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Veeraraghavan2016,
abstract = {The spatial association between proteins is crucial to understanding how they function in biological systems. Colocalization analysis of fluorescence microscopy images is widely used to assess this. However, colocalization analysis performed on two-dimensional images with diffraction-limited resolution merely indicates that the proteins are within 200-300 nm of each other in the xy-plane and within 500-700 nm of each other along the z-Axis. Here we demonstrate a novel three-dimensional quantitative analysis applicable to single-molecule positional data: stochastic optical reconstruction microscopy-based relative localization analysis (STORM-RLA). This method offers significant advantages: 1) STORM imaging affords 20-nm resolution in the xy-plane and {\textless}50 nm along the z-Axis; 2) STORM-RLA provides a quantitative assessment of the frequency and degree of overlap between clusters of colabeled proteins; and 3) STORM-RLA also calculates the precise distances between both overlapping and nonoverlapping clusters in three dimensions. Thus STORM-RLA represents a significant advance in the high-Throughput quantitative assessment of the spatial organization of proteins.},
author = {Veeraraghavan, Rengasayee and Gourdie, Robert G.},
doi = {10.1091/mbc.e16-02-0125},
file = {:home/bcardoen/Downloads/Mol.{\_}Biol.{\_}Cell-2016-Veeraraghavan-3583-90.pdf:pdf},
issn = {1059-1524},
journal = {Molecular Biology of the Cell},
number = {22},
pages = {3583--3590},
title = {{Stochastic optical reconstruction microscopy–based relative localization analysis (STORM-RLA) for quantitative nanoscale assessment of spatial protein organization}},
volume = {27},
year = {2016}
}

```
## Content
#### Research Question
colocalization analysis adapted for storm (Pauly's limit: image (200nm) analysis is not storm analysis : (20nm))

#### Contribution
Translates overlap/distance histograms from image to point SMLM space

#### Method
##### Prelude

##### Algorithm
- render points at isotropic precision
- dbscan to cluster either channel
- NN detection
- compute tesselation (3D convex hulls)
- computer overlap and histogram of distance
- registration of colors/images is key

#### Related Work

#### Data
- ventricular myocardium (real)
- no validation/contrast with random

#### Evaluation

#### Conclusion
An overlap/distance convex hull based method for directional interaction analysis.

#### Notes

#### Extra References
