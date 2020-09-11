## Title
Measurement of co-localization of objects in dual-colour confocal images
### MetaData
##### Url
http://dx.doi.org/10.1111/j.1365-2818.1993.tb03313.x
##### Type
method

##### Domain
Biology, CS

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{E.M.M1993,
author = {{E. M. M}, Manders and {F. J}, Verbeek and {J. A}, Aten},
doi = {10.1111/j.1365-2818.1993.tb03313.x},
file = {:home/bcardoen/Downloads/DocumentOpener.pdf:pdf},
isbn = {0022-2720},
journal = {Journal of Microscopy},
keywords = {co-localization,confocal microscopy,correlation,double labelling,image analysis,image reconstruction},
number = {January},
pages = {375--382},
title = {{Measurement of co-localization of objects in dual-colour confocal images}},
url = {http://dx.doi.org/10.1111/j.1365-2818.1993.tb03313.x},
volume = {169},
year = {1993}
}

```
## Content
#### Research Question
Quantify degree of colocalization of objects in confocal dual color images

#### Contribution
A measure that works in presence of background, Poisson noise, cross talk (if restored), introduces coefficients that can be used to designate overlap/colocalization independent for each challenge irrespective of the stochiometry and the per channel intensity

#### Method
Defines the fraction of colocalizing objects in the image
- Pearson from -1 to 1, hard to interpret
- $$ r = \frac{\sum R_i G_i}{ \sqrt( \sum(R_i)^2 ) \sqrt( \sum(G_i)^2 )} $$
- Ranges from 0 to 1
- Not sensitive to intensity difference in channels
- Sensitive to ratio between R/G (G can clobber R)
- let $$r^2 = k1 k2$
- let $$k1 = \frac{\sum R_i G_i}{\sum R_i^2}$
- let $$M_1 = ∑ Ri,c / \sum R_i $$ and $$Ri,c = Ri if Gi>0$$

#### Related Work
- overlap after thresholding
- binary mask overlap
- Pearson of grayscale in both (hard to interpret)
-

#### Data
Synthetic field of Guassian sources with uniform noise plus non specific binding + Poisson noise on source, equal cross talk
We constructed a Gaussian object with a diameter of 12 pixels full width at half maximum (FWHM). We then generated a 256 x 256 image with 36 objects at intervals of 32 pixels (Fig. 1A). Figure 1(E) was constructed by shifting all objects of Figure 1(A) 16 pixels to the right and 16 pixels
down.
6% uniform and 4% non-uniform background and then simulated cross-talk with cross-talk factors rr and equal to 8%. Finally, we added photon noise with an SIN of 5 dB, which corresponds to 0.3 photons per grey-value unit. These values are representative of real confocal images.
#### Evaluation
- Overlap r does not work for unbalanced object (.5 for 9/36 with 9 overlapping (should be 1))
- M1/M2 are accurate estimators
- Uniform/NUnfirom background and cross talk drive coefficients to 1 (no zero voxels)
- Poisson noise no effect for high SNR (10dB)
-

#### Conclusion


#### Notes

#### Extra References
