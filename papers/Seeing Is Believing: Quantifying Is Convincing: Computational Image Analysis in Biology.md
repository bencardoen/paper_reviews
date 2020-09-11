## Title
Seeing Is Believing: Quantifying Is Convincing: Computational Image Analysis in Biology
### MetaData
##### Url

##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
```LaTex
@book{Sbalzarini2016,
abstract = {The spatial distribution of proteins within the cell affects their capability to interact with other molecules and directly influences cellular processes and signaling. At the plasma membrane, multiple factors drive protein compartmentalization into specialized functional domains, leading to the formation of clusters in which intermolecule interactions are facilitated. Therefore, quantifying protein distributions is a necessity for understanding their regulation and function. The recent advent of super-resolution microscopy has opened up the possibility of imaging protein distributions at the nanometer scale. In parallel, new spatial analysis methods have been developed to quantify distribution patterns in super-resolution images. In this chapter, we provide an overview of super-resolution microscopy and summarize the factors influencing protein arrangements on the plasma membrane. Finally, we highlight methods for analyzing clusterization of plasma membrane proteins, including examples of their applications.},
author = {Sbalzarini, Ivo F.},
booktitle = {Advances in Anatomy Embryology and Cell Biology},
doi = {10.1007/978-3-319-28549-8_4},
file = {:home/bcardoen/Downloads/2016{\_}Book{\_}FocusOnBio-ImageInformatics.pdf:pdf},
isbn = {9783319285474},
issn = {03015556},
pages = {95--122},
title = {{Seeing Is Believing: Quantifying Is Convincing: Computational Image Analysis in Biology}},
volume = {219},
year = {2016}
}


```
## Content
#### Research Question
- how much of what is where

#### Contribution


#### Method
- Computational anaylysis
  - reproducible
  - !'it looks ok'
  - scalable
  - more powerful (pixel variations)
- inspire modeling
  - observe sufficiency
  - perturb to establish necessitiy
  - observe S in N
  - necessary
  - sufficient
    - S => N , S implies N (but P => N can exist without S)
    - N => S , S is necessary for N (N causes S)
    - N <=> S : both
- CV is no panacea for bioinformatics, need for bio-image informatics because SMLM has low SNR, complex noise, 3-4D imaging
- Require statistical sound metrics
  - there is X in experiment Y is not scientific
    - P(X|Y,alg B) = p
    - P(!X|Y, alg B) = q
- generic, open source, performant, statistically sound

###### Outline
- acquisition
  - sampling
  - noise
  - aberrations
  - blinking
  - density
- processing artifacts
  - precision
  - inversion
  - fp
  - segmentation/registation
- model assumptions
- object
  - annotate : object is a (nucleus)
  - grammar : nuclei are grouped
  - semantics : nuclei + pb => C

- all uncertainties should be
  - known
  - bounded effect on downstream

- forward problem
  - specimen to image to object
- backward problem/inverse
  - object to image to specimen
  - ill posed, no unique solution, source space
  - how much prior knowledge is required for analysis of source space
  - inverse problem is inference task
    - infer shape, location, distribution and interaction from acq
      - Bayesian
        - conclusion that explains the data
        - maximize P(seg | img) ~ P(img | segment) x Prior
      - frequentist
        - distribution of the data explains the data
      - evidence based versus Bayesian based
        - belief function
        - Bayesian probablity function = belief function
- filtered approaches
  - lin/nlin transformations with optional prior
    - e.g. PSF peaks
- ML
  - use features as input
  - can be combined with filtered
- model based paradigm
  - compare model with image (Gold standard)
    - key is how to compare
    - composite model : object + imaging + noise
- optimizing the model to fit the data!!
  - global models
  - a model should only be used to sharpen the research question
- challenges
  - multidimensional large scale data
    - CMOS produce ~200TB per day, outstripping soft/hard ware
    - streaming to HPC is more efficient than storing and rerunning
    - require parallel / distributed algorithms
    - CI/uncertainty of analysis needs to be known and stored
      - reproducing raw image is no longer feasible
  - uncertainty quantification
    - a hard problem
    - CI to probability is in general not known (normalization is unknown)
    - when an algorithm terminates, how far is it from the solution ?
    - what is the effect of the prior ?
    - impact of noise/artifacts
      - what is the impact, and is additive/multiplicative ...
      - deconvolution is example of amplification of noise
      - global optimum != local optimum of subset
      - quantify the downstream effect of artifacts
    - global optimal (proven) methods
    - theoretical results (Cramer-Rao holds for points, not structures)
    - transform results into evidence with CI
    - diversity solutions, branching alternate solutions equally probable

  - generic algorithms
    - combine of x tasks
      - ill posed problems merged tend to regularize in contrast with sequential, because the output space is reduced (hence fewer acceptable solutions)
    - increase class of problems algorithm can deal with
      - filter is bound to prior
      - ml retrains, model switch out
    - parameter free algorithm
      - robust, adaptive, fast
  - collaborative open source software
    - research software grows, maintenance is problematic
    - models
      - scripting
      - gui
      - libraries
      - 
  - databases
  - annotation systems

  - testing/benchmarking


#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
