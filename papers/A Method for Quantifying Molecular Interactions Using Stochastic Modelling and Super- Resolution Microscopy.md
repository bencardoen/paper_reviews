## Title
A Method for Quantifying Molecular Interactions Using Stochastic Modelling and Super- Resolution Microscopy
### MetaData
##### Url
10.1038/s41598-017-14922-8
##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Bermudez-Hernandez2017,
abstract = {{\textcopyright} 2017 The Author(s). We introduce the Interaction Factor (IF), a measure for quantifying the interaction of molecular clusters in super-resolution microscopy images. The IF is robust in the sense that it is independent of cluster density, and it only depends on the extent of the pair-wise interaction between different types of molecular clusters in the image. The IF for a single or a collection of images is estimated by first using stochastic modelling where the locations of clusters in the images are repeatedly randomized to estimate the distribution of the overlaps between the clusters in the absence of interaction (IF = 0). Second, an analytical form of the relationship between IF and the overlap (which has the random overlap as its only parameter) is used to estimate the IF for the experimentally observed overlap. The advantage of IF compared to conventional methods to quantify interaction in microscopy images is that it is insensitive to changing cluster density and is an absolute measure of interaction, making the interpretation of experiments easier. We validate the IF method by using both simulated and experimental data and provide an ImageJ plugin for determining the IF of an image.},
author = {Bermudez-Hernandez, Keria and Keegan, Sarah and Whelan, Donna R. and Reid, Dylan A. and Zagelbaum, Jennifer and Yin, Yandong and Ma, Sisi and Rothenberg, Eli and Feny{\"{o}}, David},
doi = {10.1038/s41598-017-14922-8},
file = {:home/bcardoen/Downloads/s41598-017-14922-8.pdf:pdf},
isbn = {4159801714},
issn = {20452322},
journal = {Scientific Reports},
number = {1},
pages = {1--13},
title = {{A Method for Quantifying Molecular Interactions Using Stochastic Modelling and Super-Resolution Microscopy}},
volume = {7},
year = {2017}
}


```
## Content
#### Research Question
Quantify interaction in SMLM images

#### Contribution
Interpretable density insensitive IF for SMLM images

#### Method
Input: segmented color smlm images with 1 color as reference
Control: random simulation
IF is based on overlap which is less relevant with Pauli's principle coming close
- otsu segmented clusters (2d)
- 20nm pixels
- does not account for context (overlap by state likelihood)

#### Related Work


#### Data


#### Evaluation


#### Conclusion
Overlap factor compared with random simulation, pixel based.

#### Notes

#### Extra References
