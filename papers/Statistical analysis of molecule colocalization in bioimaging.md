## Title
Statistical analysis of molecule colocalization in bioimaging
### MetaData
##### Url
10.1002/cyto.a.22629
##### Type
review

##### Domain
Biology, CS, statistics

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Lagache2015,
abstract = {{\textcopyright} 2015 International Society for Advancement of Cytometry. The quantitative analysis of molecule interactions in bioimaging is key for understanding the molecular orchestration of cellular processes and is generally achieved through the study of the spatial colocalization between the different populations of molecules. Colocalization methods are traditionally divided into pixel-based methods that measure global correlation coefficients from the overlap between pixel intensities in different color channels, and object-based methods that first segment molecule spots and then analyze their spatial distributions with second-order statistics. Here, we present a review of such colocalization methods and give a quantitative comparison of their relative merits in different types of biological applications and contexts. We show on synthetic and biological images that object-based methods are more robust statistically than pixel-based methods, and allow moreover to quantify accurately the number of colocalized molecules.},
author = {Lagache, Thibault and Sauvonnet, Nathalie and Danglot, Lydia and Olivo-Marin, Jean Christophe},
doi = {10.1002/cyto.a.22629},
file = {:home/bcardoen/Downloads/Lagache{\_}et{\_}al-2015-Cytometry{\_}Part{\_}A.pdf:pdf},
issn = {15524930},
journal = {Cytometry Part A},
keywords = {Colocalization,Endocytosis,Light microscopy,Quantitative measurements,Spatial statistics},
mendeley-groups = {SRM},
number = {6},
pages = {568--579},
title = {{Statistical analysis of molecule colocalization in bioimaging}},
volume = {87},
year = {2015}
}

```
## Content
#### Research Question
Overview of statistical analysis methods in SMLM

#### Contribution


#### Method
- FRET : can't be used if molecules too large or macromolecular complex, or when molecules only colocalize spatially in cellular microdomains such as membrane domains or intracellular organelles
- Fluorescence Cross Correlation Spectroscopy (FCCS) : FCCS cannot be applied when one of the molecules is docked or immobilized. Last but not least, these methods are difficult to use for the analysis of the interaction between more than two different molecule populations
##### Measures
- Robustness : is x significant? (exclude by chance)
- Accuracy of quantification : Colocalization -> distance and percentage of colocalized?

###### Covered methods
- Pearson (pixel) : to test significance shift image by x pixels and measure again
- Scrambling : pixel/block/spot scrambling. Both pixel and block scrambling break autocorrelation, so can lead to false positives, it's better to use spot scrambling (simulate random spots)
- Scrambling is expensive
  - intensity correlation quotient as alternative
  - http://www.jneurosci.org/content/24/16/4070#sec-2
  - P[ICQ>0] = 0.5 test only works when random signal is symmetric (which it isn't) with low intensity signal
SRM forces away from pixel based methods
- SRM Marked Point Process (mark = color)
  - described by 2nd order characteristics
    - distance to nearest neighbour
      - $$S(r)=1/n1 \sum_{i=1}^n1 1(di<r) $$
      - Null = $$ 1-e^{-n2/omega * B(r)}
        - B(r) is area or sphere, omega is volume
        - boundary correction difficult, so tested by MC
    - Ripleys
    - need correction for FOV boundary (fewer neighbours at edge), in practice not used for NN, a lot of them are used in Ripleys
      - Ripleys and NN need multiscale (which r?)
      - Chi Square with Ripleys
    - Gibbs process modelling


#### Related Work


#### Data
Synthetic Gaussian with noise filtered by wavelet filter.

#### Evaluation


#### Conclusion


#### Notes

#### Extra References
