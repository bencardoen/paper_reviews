## Title

Accounting for limited detection efficiency and localization precision in cluster analysis in single molecule localization microscopy

### MetaData
##### Url

10.1371/journal.pone.0118767

##### Type
Method

##### Domain

CS, Biology, Math

##### Keywords 
 Error, uncertainty


##### Cite

```LaTex


```
## Content
#### Research Question
We provide analytical methods to estimate the effect of these errors in cluster analysis and to correct for them. 

#### Contribution
* Adapts PCF, LRR to error in palm (extends to SMLM)

#### Method

* LRR is invariant to spatial subsampling (effciency of reconstruction) if subsampling is homogeneous

* Localization method

  * Find true locations of fluorophore emitters

* LRR, PCF are invariant to random (independent) subsampling (efficiency)

  * IFF it is homogenuous

* K, PCF are adapted with given assumption of independent error in measurement

* Localization

  * Assume cluster C with K points

    * X_i to k are recorded locations
    * Find cluster center x (mean) $x_u$
    * Find variance $\sigma_{x}^2 = 1/K \sum_{i=1}^K \sigma_{x,i}^2  $ # Mean error
    * Estimate of spread : $1/(k-1) \sum_{i=1}^K (x_i - x_u)  - \sigma__{x}^2$ 
      * Omit - if <0
    * $x_{true i} = x_{mean} + \frac{\sigma_x}{\sqrt{\sigma)_x^2 + \sigma_{xi}^2}} {x_i - x_u}

  * Assumes K is known




#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
