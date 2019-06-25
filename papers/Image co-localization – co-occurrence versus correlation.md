## Title
Image co-localization – co-occurrence versus correlation
### MetaData
##### Url
10.1242/jcs.211847
##### Type
review
##### Domain
Biology, CS

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Aaron2018,
abstract = {Fluorescence image co-localization analysis is widely utilized to suggest biomolecular interaction. However, there exists some confusion as to its correct implementation and interpretation. In reality, co-localization analysis consists of at least two distinct sets of methods, termed co-occurrence and correlation. Each approach has inherent and often contrasting strengths and weaknesses. Yet, neither one can be considered to always be preferable for any given application. Rather, each method is most appropriate for answering different types of biological question. This Review discusses the main factors affecting multicolor image co-occurrence and correlation analysis, while giving insight into the types of biological behavior that are better suited to one approach or the other. Further, the limits of pixel-based co-localization analysis are discussed in the context of increasingly popular super-resolution imaging techniques.},
author = {Aaron, Jesse S. and Taylor, Aaron B. and Chew, Teng-Leong},
doi = {10.1242/jcs.211847},
file = {:home/bcardoen/Downloads/jcs211847.full (1).pdf:pdf},
issn = {0021-9533},
journal = {Journal of Cell Science},
keywords = {biological system,co-localization,co-localization can be,fluorescence microscopy,image analysis,manders,more strategically employed,pearson,pitfalls of,this review explores how,we outline strengths and},
mendeley-groups = {SRM,doublelabelling},
number = {3},
pages = {jcs211847},
title = {{Image co-localization – co-occurrence versus correlation}},
volume = {131},
year = {2018}
}


```
## Content
#### Research Question
How to analyze multicolor fluoresence micrscopy

#### Contribution
Summarized contribution(s)

#### Method
- Only FRET (Forster resonant energy transfer) can determine/measure molecular interactions
- CR/CO can infer relationships
Both/either occur, does not describe relation, but presence in a organelle
*WARNING*
- This serves to illustrate that correlation and co-occurrence are independent phenomena, as they measure distinct behavior in an image pair. While co-occurrence gauges the overlap between signals in two images, correlation measures the relationship between those signals *in overlapping areas*.
##### Co-occurrence

- Simplest form is thresholding (Otsu) and Jaccard
- Mander's : inflated by background or ns signal, insensitive to SNR
  - Either fix with preprocessing
  - Or scramble image (rearrange pixels in blocks)
    - determine block size with image autocorrelation
  - Compare scrambled R with unscrambled G and check if MOC > MOC_s, if 95% then stat valid
  - Dunn et al: Rotate 90 and compare (not statistical)



##### Correlation
Correlation analysis is most applicable when assessing a functional or stoichiometric relationship between two overlapping species, but does not specifiy co-occurrence in spatial dimension.

- PCC (requires equality of sample (thresholded pixels))
  - PCC : images input is critical, on a scatterplot linearity is no longer true, so PCC is truncated
  - PCC is affected (reduced) by decreasing SNR
  - Costes's significance test:
    - PCC on >= threshold AND below
      - if PCC < tends to zero, then assumption of noise
      - for non CC there is no elbow point
  - PCC is not sensitive to uniform background, (broadens the line)

- Spearman
  - If relation is not linear, PCC fails (+- 1 is linear)
  - Spearman is correlation between ranked
    - rank is by order of value > threshold (2,5,3,7 with th =2 -> 2,1,3 )
    - less sensitive to saturation effects

###### In SMLM
- This serves to illustrate that correlation and co-occurrence are independent phenomena, as they measure distinct behavior in an image pair. While co-occurrence gauges the overlap between signals in two images, correlation measures the relationship between those signals in overlapping areas.
- Coordinate based colocalization analysis (CBC)
  - $$ D_{x, x_i} = N_{x_i, x}(r) / N_{x_i, x}(Rmax) *  Rmax^2 / r^2 $$
  - Rmax > expected interaction distance
  - radius r (param)
  - N_{x_i, x}(r) = number of localizations of color x with <= r of x_i
  - SRCC(N_{x_i, x}(r), N_{x_i, y}(r))
  - CBC is a map
- Ripley
  - L function to find distance of interaction/repulsion (local maxima/minima)
- Sensitive to parameters, complementary
###### Postprocessing
- Correction for chromatic aberration
- Focal plane drift
- non biological signal
- background
- coregistration

###### Final
- SRM: in focus only so no correct, distance tends to zero, spatial statistical approaches favored instead of image, no dynamics, computationally expensive


#### Related Work

#### Data


#### Evaluation

#### Conclusion

#### Notes

#### Extra References
