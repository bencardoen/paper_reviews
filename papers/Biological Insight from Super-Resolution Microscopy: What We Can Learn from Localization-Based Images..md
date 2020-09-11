## Title
Biological Insight from Super-Resolution Microscopy: What We Can Learn from Localization-Based Images.

### MetaData
##### Url
https://www-annualreviews-org.proxy.lib.sfu.ca/doi/pdf/10.1146/annurev-biochem-060815-014801
##### Type
review

##### Domain
Biology, CS, Mathematics

##### Keywords
smlm, storm, palm, image, interaction, colocalization



##### Cite
e.g. BibLatex
```LaTex

@article{Baddeley2018,
abstract = {Super-resolution optical imaging based on the switching and localization of individual fluorescent molecules [photoactivated localization microscopy (PALM), stochastic optical reconstruction microscopy (STORM), etc.] has evolved remarkably over the last decade. Originally driven by pushing technological limits, it has become a tool of biological discovery. The initial demand for impressive pictures showing well-studied biological structures has been replaced by a need for quantitative, reliable data providing dependable evidence for specific unresolved biological hypotheses. In this review, we highlight applications that showcase this development, identify the features that led to their success, and discuss remaining challenges and difficulties. In this context, we consider the complex topic of defining resolution for this imaging modality and address some of the more common analytical methods used with this data.},
author = {Baddeley, David and Bewersdorf, Joerg},
doi = {10.1146/annurev-biochem},
file = {:home/bcardoen/.local/share/data/Mendeley Ltd./Mendeley Desktop/Downloaded/Baddeley, Bewersdorf - 2018 - Biological Insight from Super-Resolution Microscopy What We Can Learn from Localization-Based Images.pdf:pdf},
keywords = {PAINT,PALM,STORM,nanoscopy,quantitative analysis,single-molecule localization microscopy},
mendeley-groups = {SRM},
title = {{Biological Insight from Super-Resolution Microscopy: What We Can Learn from Localization-Based Images}},
url = {https://doi.org/10.1146/annurev-biochem-},
year = {2018}
}

```
## Content
#### Research Question
we highlight applications that showcase image to analysis methods, identify the features that led to their success, and discuss remaining challenges and difficulties
#### Contribution
Overview of methods (analysis) in SMLM and their challenges (in addition to resolution impact)

#### Method
##### Imaging methods
STORM
PALM
GSDIM
PAINT : diffuse mobile are invisible (no signle specific PSF until they bind)
##### Objects
- well separated similar structures (e.g. nanopores) (1)
- well separated but low digree of similarity --> individual analysis (2)
- complex proximate structures : incomplete reconstruction (3)

- Biological studies that can exploit these criteria of isolation and the ability to be averaged—
either through the intrinsic nature of the structure studied or by careful choice of experimental conditions and metrics—lend themselves to the generation of robust quantitative results despite limitations on labeling efficiencies inherent to the current state of the art. Not surprisingly most high impact publications fall into this field
- Current labeling chemistries, be it antibodies, SNAP, CLIP, or Halo tags (41, 42), or direct fusion proteins, label only a fraction of the target, and dye photochemistry further limits the portion of the labels one can actually see.
- The statistical nature of the spatial distribution of localizations (see
Section 4.4) can lead to the random formation of intriguing spatial arrangements and make it
very tempting to overinterpret the images.
-The hardest class ofstructures to image are arguably those that either are not easily distinguishable from background or neighboring structures, or are extended and complex with features ofinterest in the 10- to 50-nm range. Examples include the Golgi complex in typical mammalian cells or chromatin in the interphase nucleus. These structures test the limits of localization microscopy, needing both exceptionally high labeling density and localization precision.

1: Data averaging and data reduction
2: Autocorrelation function --> Autocorrelation, also known as serial correlation, is the correlation of a signal with a delayed copy of itself as a function of delay. Informally, it is the similarity between observations as a function of the time lag between them.
3: Extremely difficult, focus on simulated controls

##### Interaction
- Interaction as a discrete (binary or higher)
- classification of interating/non-interacting pools of molecules
Approaches
 - thresholding of intensities of both colours
 - Pearson correlation of angular alignment (compared to random)
 - particle tracking can differentiate (diffuse to concentrated)
##### Resolution
*Precision*
- Two key concepts that underlie resolution
in SMLM are the localization precision and the localization density. Ultimately, however, the
concept of resolution might even depend on what one is trying to determine from the sample.
- Cramer-Rao lower bound (CRLB)
- For Gaussian PSF function of std of PSF, a pixel size, b background photons per pixel, N photon count
- Thompson
- Mortensen et al improve on Thompson
- The actual localization precision achieved will therefore always be worse and, in particular,
depends strongly on the choice of localization algorithm.
- CRLB is estimated based on the PSF, and will be worse in reality because it's influenced by (non convergence) of estimation algorithms (dangerous with GPU)
- ... For example, a localization precision of 12 nm means that the resolution in a reconstructed image will be no better than 28 nm.
*Density*
-The relationship between localization density and resolution is, however, complex.
- TheNyquist sampling criterion describes which spatial frequencies can be reconstructed when
taking regularly spaced real values from a signal; however, the criterion is inadequate in SMLM, as localizations are not samples in the classical sense but rather are events that are neither regularly spaced nor have a value (other than 1) associated with them. Empirically, it seems that for a given resolution the distance between neighboring localizations should be significantly less than that indicated by a naive application of the Nyquist limit, with a factor of five times higher sampling having been proposed (69, 70).
-  Disadvantages stem from the fact that FRC curves depend on the shape of the imaged
object since FRC implicitly measures the power spectrum of the object (i.e., how self-similar
it is at different length scales). Images dominated by complex, extended objects can yield much
worse FRC resolution values than images primarily containing small clusters scattered across the
field of view.
*Effect of Noise*
- Rose criterion : d = 5 / C sqrt(n)  // d is diameter of smallest resolvable splot, n is areal density of photons in background (localizations) and C is contrast (n - n spot/ n)
- SNR = n/sqrt(n) = sqrt(n)
-  Sparrow : probability of observing a dip between two point objects as a function of their separation (in units of the localization precision σ). Significantly more localizations are required than would be expected from the Nyquist sampling criterion. For a 95% significance cutoff, the 2.35 σ resolution predicted by localization precision alone is achieved only in the limit of extremely high
localization precision σ). Significantly more localizations are required than would be expected from the Nyquist sampling criterion. For a 95% significance cutoff, the 2.35 σ resolution predicted by localization precision alone is achieved only in the limit of extremely high (?100) localization numbers.
a 95% significance cutoff, the 2.35 σ resolution predicted by localization precision alone is achieved only in the limit of extremely high (?100) localization numbers.
- Regardless of how resolution is quantified, two key features become apparent: Resolution in
SMLM is inherently a function of the structure being imaged as well as of the microscope, and
labeling density is critical—most likely more so than previously appreciated.
*Hypothesis testing*
- Based on the underlying structure define a hypthesis
##### Counting
Overcounting due to multiple blinking, undercounting due to ineffective labelling, localization error, crossbleeding, ...
##### Clustering
Grouping of localizations to describe
- Ripley (K/L) to describe, compared to random, the avg no of mol in r distance to target
- Depends on consistency of shape and size
- Classical
- DBSCAN
- Thresholding in images
- Tessellation based density estimation are more robust than Gaussian
- Bayesian
##### Colocalization
- It is physically impossible for two targets to occupy the same space, meaning that on a molecular-length scale colocalization (as defined byPearson’s or Manders’ coefficients) is zero (or negative) by
definition. As the resolution approaches the molecular scale, one observes very low colocalization, regardless of the target. The second major issue one confronts when applying colocalization methods to SMLM images is the large degree of stochasticity observed in many techniques (see
Section 4).

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
