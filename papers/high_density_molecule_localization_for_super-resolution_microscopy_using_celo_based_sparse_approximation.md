## Title
High density molecule localization for super-resolution microscopy using CEL0 based sparse approximation
### MetaData
##### Url
[url](https://www.rug.nl/research/portal/publications/high-density-molecule-localization-for-superresolution-microscopy-using-cel0-based-sparse-approximation(5c7223c3-104d-46bf-8e52-ffd60f182d03)/export.html)
##### Type
method 

##### Domain
Optics, CS, Biology, Chemistry

##### Keywords 
smlm, celo, srm, approximation, sparse

##### Cite
e.g. BibLatex
```LaTex
@inproceedings{Gazagnes2017,
author = {Gazagnes, Simon and Soubies, Emmanuel and Blanc-Feraud, Laure},
booktitle = {2017 IEEE 14th International Symposium on Biomedical Imaging (ISBI 2017)},
doi = {10.1109/ISBI.2017.7950460},
file = {:home/bcardoen/Documents/Mendeley Desktop/ISBI{\_}Gazagnes2017.pdf:pdf},
isbn = {978-1-5090-1172-8},
mendeley-groups = {SRM},
month = {apr},
pages = {28--31},
publisher = {IEEE},
title = {{High density molecule localization for super-resolution microscopy using CEL0 based sparse approximation}},
url = {http://ieeexplore.ieee.org/document/7950460/},
year = {2017}
}
```
## Content
#### Research Question
Photon to localization in SMLM.

#### Contribution
Highly accurate localization method for high density (where everyone else fails)

#### Method
Discretized input from continuous input.
Regularization induced sparse solution of LSQ.
Minimize location difference, intensity difference, solution sparsity.

Problem in NP Hard

Relaxation with IRL1 algorithm and CEL0 norm approximation.

##### Celo
L0 norm of solution : binary sum of points

Shown that argmin CEL0 is superset of argmin l0.

IRL1 is proven convergent, minimizer is FISTA. 


#### Related Work
 > DAOSTORM (best)

#### Data
Synthetic and benchmark

#### Evaluation
TP, FP, FN where match if x, x' < e

Jaccard : TP  / (TP + FP + FN) * 100

SNR :  10 x log_10 ( L2(True Loc) / L2 ( Image - True Loc))

512 by 512 image input , 25nm pixel

PSF 150nm

Image : 128x128 (L=4)

Tolerance = 100nm (1/3 FWHM)

###### Results
J = 85 at 10 SNR, 2 density
J = 40 at 10 SNR, 10 density

Best tolerance (jaccard 40) is 100nm (factor 3 better)

Finer results

#### Conclusion
!! Only best result retained ?

#### Notes

#### Extra References

[FISTA](https://blogs.princeton.edu/imabandit/2013/04/11/orf523-ista-and-fista/)
