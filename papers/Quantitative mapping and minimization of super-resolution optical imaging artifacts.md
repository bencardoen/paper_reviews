## Title
Quantitative mapping and minimization of super-resolution optical imaging artifacts
### MetaData
##### Url
10.1038/nmeth.4605
##### Type
method

##### Domain
Biology, CS

##### Keywords
smlm, resolution, precision, image quality, confidence



##### Cite
e.g. BibLatex
```LaTex
@article{Culley2018,
abstract = {This paper reports an approach to map errors in super-resolution images, based on quantitative comparison to diffraction-limited equivalents.},
author = {Culley, Si{\^{a}}n and Albrecht, David and Jacobs, Caron and Pereira, Pedro Matos and Leterrier, Christophe and Mercer, Jason and Henriques, Ricardo},
doi = {10.1038/nmeth.4605},
file = {:home/bcardoen/Downloads/nmeth.4605.pdf:pdf},
issn = {15487105},
journal = {Nature Methods},
number = {4},
title = {{Quantitative mapping and minimization of super-resolution optical imaging artifacts}},
volume = {15},
year = {2018}
}

```
## Content
#### Research Question
Compare widefield with SR image

#### Contribution
A pipeline approach to map in 2D the localization errors in SR

#### Method
- Input : SR image, widefield image, resolution scaling function image
- Output : Error map (2D) overlayed on SR
- Metrics:
  - pixel wise error (abs diff) of aligned intensity
  - RSE : rmse of reference and resolution scaled images
  - RSP : resolution scaled pearson (-1/+1)
  - FRC (just applied)
- RSF is a convolution that aligns the intensity between SR and widefield (dangerous)

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
