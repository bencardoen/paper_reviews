## Title

On characterizing protein spatial clusters with correlation approaches

### MetaData
##### Url

http://dx.doi.org/10.1038/srep31164

##### Type
comparative analysis

##### Domain

Math, Biology, CS

##### Keywords 
Ripley, PCF, clusters, SMLM, SRM


##### Cite

```LaTex


```
## Content
#### Research Question
Ripley vs PCF, how does the clustering of the data affect the analysis?

#### Contribution


#### Method
* Clustering can reveal protein functionality in signaling, transcription, interaction
* Strength, scale, density, ... characterizes clustering
* Two types
  * Segmentation and characterization of clustering
  * 2nd order spatial summary functions
    * parameter free
    * interactions at multiple spatial scales
    * dense/sparse compatible
    * physical interpretation
    * extensions incorporating error models
* SMLM errors
  * artifacts due to single fluorophore blinking
  * low retrieval
  * 10-50nm localization uncertainty (FWHM)
* Ripley : radius value that corresponds with maximum of  L(r) - r function (empirical scale estimator)
* Pair correlation function, functional approximation of g(r) as exponential function
  * Results in estimators for cluster size, amplitude/strength, and molucles per cluster
* Both are 2nd order estimators of correlation, 
* Free of underlying cluster process
* Ripley K
  * K(r) = $1 / \rho E[M(r)]$ (2D points)
    * rho is density, mean points per unit area
    * M(r) is density of points within r of random chosen point
  * Besag L(r) -r 
    * L(r) - r = $\sqrt(\frac{K(r)}{\pi}) - r $  # Measures cluster strength at r
  * PCF
    * $g(r) = \frac{K'(r)}{2 \pi r}$
    * $g_a (r) = 1 + \exp{-r / d} $ d is radius of cluster, a is amplitude (density)
    * $N_{points in cluster} = 1 + \rho \int_{0}^{\infty} (g(r) - 1)2 \pi r dr
* Can incorporate background clustering model

#### Related Work


#### Data


#### Evaluation


#### Conclusion
* We find that crucial independent parameters of clustering, such as the number of molecules per cluster, may not be reflected in the L(r) − r curves
* Our results illustrate that the ratio of radius of maximal aggregation (from L(r) − r curves) to the true cluster size nonlinearly depends on the true cluster size as well as the number of clusters per unit area (or corresponding parameters, such as amplitude) for all the models considered. While we were able to derive theoretical lower bounds for this ratio, we found that the ratio could be arbitrarily large depending on the parameters and models, illustrating that the radius of maximal aggregation is not always indicative of the true cluster size.
* PCF : . It was found that the relationship between estimates and true parameters were found to be linear, and that the bias is limited to ±100% of true parameter values for the models we considered. These results apply to model independent measures such as number of molecules per cluster.

#### Notes

#### Extra References
