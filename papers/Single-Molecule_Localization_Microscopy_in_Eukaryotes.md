## Title
Single-Molecule Localization Microscopy in Eukaryotes
### MetaData
##### Url
10.1021/acs.chemrev.6b00667
##### Type
review

##### Domain
Biology, Chemistry


##### Keywords
SMLM, Eukaryotes

##### Cite

```LaTex


```
## Content
#### Research Question
Review of methods in SMLM

#### Contribution
* Full review

#### Method
* emission --> blurry spot in pixelated view
* fwhm of spot is lamdba/2 (wavelength)
* Precisions ~ sigma/sqrt(N)
* spatial resolution of an SMLM image cannot be expressed with a single number and further depends on the local structural complexity of a particular cellular feature
* SR Image is :
    * Hist Image at subpixel (pixel = res)
    * Convolve points with Gaussian with sigma = res
* Conversion rate (>94 for tubules), number of fluorophores in off state
* Not sufficient for complex dense structures
* ground-state depletion microscopy followed by individual molecule return (GSDIM)
* FWHM = 2 sqrt(2 ln 2) sigma, measure width of Gaussian where intensity is half of maximum
* Total internal reflection fluorescence (TIRF) microscopy can be used to restrict irradiation to the basal cell membrane and reduce photodamage.
* Indicators of photodamage are abnormal cell morphology, detachment from the substrate, appearance of granules on the surface of the cell, condensation of the nucleus, and strongly increased autofluorescence.
* DNA- PAINT is ideally suited for multiplexing, as it does not rely on photoswitchable fluorophores; the binding specificity is determined by using different oligonucleotide sequences labeled with spectrally distinct dyes
* Analysis:
    * Precision/resolution
    * Ripley's K/L/H : difference between random / data distribution as clustering
    * DBSCAN (cluster within e, d)
    * Coordinate based colocalization (CBC): spatial organization of 2 proteins
    * CBC on single color avoids thresholding
        * Compute density gradient, correlate density gradient correlation

#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
