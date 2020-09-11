## Title

### MetaData
##### Url
[url](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=PMC4494126)

##### Type
review 

##### Domain
CS, Physics, Chemistry, Biology

##### Keywords 
smlm, storm, palm, optics, microscopy, psf, gaussian

##### Cite
e.g. BibLatex
```LaTex
@article{Ober2015,
abstract = {Single molecule microscopy is a relatively new optical microscopy technique that allows the detection of individual molecules such as proteins in a cellular context. This technique has generated significant interest among biologists, biophysicists and biochemists, as it holds the promise to provide novel insights into subcellular processes and structures that otherwise cannot be gained through traditional experimental approaches. Single molecule experiments place stringent demands on experimental and algorithmic tools due to the low signal levels and the presence of significant extraneous noise sources. Consequently, this has necessitated the use of advanced statistical signal and image processing techniques for the design and analysis of single molecule experiments. In this tutorial paper, we provide an overview of single molecule microscopy from early works to current applications and challenges. Specific emphasis will be on the quantitative aspects of this imaging modality, in particular single molecule localization and resolvability, which will be discussed from an information theoretic perspective. We review the stochastic framework for image formation, different types of estimation techniques and expressions for the Fisher information matrix. We also discuss several open problems in the field that demand highly non-trivial signal processing algorithms.},
author = {Ober, Raimund J and Tahmasbi, Amir and Ram, Sripad and Lin, Zhiping and Ward, E Sally},
doi = {10.1109/MSP.2014.2353664},
file = {:home/bcardoen/Documents/Mendeley Desktop/Ober et al. - 2015 - Quantitative Aspects of Single Molecule Microscopy.pdf:pdf},
issn = {1053-5888},
journal = {IEEE signal processing magazine},
mendeley-groups = {geometry},
month = {jan},
number = {1},
pages = {58--69},
pmid = {26167102},
publisher = {NIH Public Access},
title = {{Quantitative Aspects of Single Molecule Microscopy.}},
url = {http://www.ncbi.nlm.nih.gov/pubmed/26167102 http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=PMC4494126},
volume = {32},
year = {2015}
}

```
## Content
#### Research Question
Review of computational aspects of superresolution microscopy.

#### Contribution
Overview of the field

#### Method

###### Physics
Camera is linear shift time invariant system: Linear relation between in, out where parameters do not change over time.

* Physical model: Image is continuous probability (2D) distribution (Poisson per emitter) of object at time.
* Pixellated due to camera
* Practical model differs from camera type
* Typically combined pdf based on Poisson(emissions) and Gaussian(capture)
* Typical min LSE, but MLE is better
* Different PSFS for different type, Gaussian assumed to work best as generic, but specific complex fits deal with out of focus etc

##### Estimation, resolution, information
How do you quantify output of the microscope?

###### XY
* Accuracy (how precise is a single localization)?, lowest possible std
* [Resolution](https://courses.lumenlearning.com/austincc-physics2/chapter/27-6-limits-of-resolution-the-rayleigh-criterion/), at what limit distance can 2 objects be separated?

For sparse data:
* How well can two points be resolved (e.g. distance): std(distance) decreases as photon count increases (closed form)
* The smaller the distance, the more photons you need

For dense data:
* Fourier Ring Correlation

###### Z
* Out of focus (far away) is almost impossible to quantify
* Close at focal plane
* Depth discrimination problem: close to focal plane
* As a result astygmatic lens is used, depending on elongation (sign and magnitude) the actual Z position is retrieved
* Double helix, rotation of helix is used to find Z, but closed form analytical expression of resolution is not possible (approx only)
* iPalm : Z by changing imaging process
* MUM : Look at slices of planes, then sum Z


##### Multi-Emitter problem
* Assumption of single emitter is only stochastisc
* How do we differentiate between single and multi-emitter, and what metrics are involved, ie how do we estimate multi emitters?
 



#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes
* Resolution and other software

#### Extra References
