## Title
Turning single-molecule localization microscopy into a quantitative bioanalytical tool
### MetaData
##### Url

##### Type
review,

##### Domain
Biology

##### Keywords
SMLM, clustering, statistics, quantitative, data analysis


##### Cite

```LaTex


```
## Content
#### Research Question
Review of quantitative methods in SMLM

#### Contribution
These methods strive to extract results describing the patterning, topography and geometry of subdiffraction features using these super-resolution methods, rather than treating SMLM data as a prelude to a high-resolution image.

#### Method
* Pair correlation
* DBSCAN
* Voronoi/Delaunay as density estimation
* Nearest neighbour: Clark–Evans statistic (random has value of 1 , < 1 is dispersed, > 1 is clustered)
    * Fails for SMLM because fluorophores have their own sparsity distribution
* Ripley K / Pair Correlation:
    * Cluster shapes, cluster has RK or PC score, PC is more robust to self clustering
* Per cluster methods
    * Bayesian cluster identification : evaluated w.r.t. prior model
    * DBSCAN
        * parameter sensitive
        * no model assumption
        * fails for varying density
    * Tesselation and use features of the faces as segmentation
* Colocalized clustering
* Counting using temporal dimension
    * Counting should be robust against high variation in time
* Precision is per point, not global
* Ex nihilo morphological sampling 5-7 fold Nyquist lower bound is minimum necessary
* Causes of undercounting
    * Focal drift
    * Folding efficiency of GFP
    * masking/quenching of neighbouring fluorophores
    * undercounting decreases over time
    * detection efficiency is
    * fluorophore detection efficiency is ~ <40%
* Future direction
    * Exact counting under all conditions
    * Use per point precision in analysis
#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
