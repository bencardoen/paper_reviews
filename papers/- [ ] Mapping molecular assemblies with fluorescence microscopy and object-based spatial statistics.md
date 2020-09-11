## Title
Mapping molecular assemblies with fluorescence microscopy and object-based spatial statistics

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
@article{Lagache2018,
author = {Lagache, Thibault and Grassart, Alexandre and Dallongeville, St{\'{e}}phane and Faklaris, Orestis and Sauvonnet, Nathalie and Dufour, Alexandre and Danglot, Lydia and Olivo-Marin, Jean-Christophe},
doi = {10.1038/s41467-018-03053-x},
file = {:home/bcardoen/Downloads/s41467-018-03053-x (2).pdf:pdf},
issn = {2041-1723},
journal = {Nature Communications},
month = {dec},
number = {1},
pages = {698},
title = {{Mapping molecular assemblies with fluorescence microscopy and object-based spatial statistics}},
url = {http://www.nature.com/articles/s41467-018-03053-x},
volume = {9},
year = {2018}
}

```
## Content
#### Research Question
Our method considers cellular geometry and densities of molecules to provide statistical maps of isolated and associated (coupled) molecules.

#### Contribution
Spots in image based interaction (coupling) analysis with statistical significance addition.

#### Method
##### Prelude
- Interaction scales : phys 1-10, complexes 10-100, copresence in domains 100-500
Input: SR image with spot detection
- Boundary correction
- Fluorescent spots are automatically detected and represented with a Marked Point Process: the point is the spot’s localisation (centre of mass or intensity) and the mark embraces morphological properties as the size and the colour of the spot.
- Uses frequency and deviation from random expectation with ring based Ripleys to determine coupling probablity

#### Related Work


#### Data
Neurons, synthetic in several microscopes

#### Evaluation


#### Conclusion
Ripley ring based coupling distance/probability measure for image and localization based, given clustering

#### Notes

#### Extra References
