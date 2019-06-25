## Title
Visualization of Localization Microscopy Data
David
### MetaData
##### Url
10.1017/s143192760999122x
##### Type
method, review

##### Domain
Biology, CS

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
your cite code here

```
## Content
#### Research Question
Translate positions to an image
#### Contribution
-overview of existing techniques contrasting their own contributions

#### Method
##### Impact of accuracy
- effective resolution
- SR is multiresolution
- labelling density is key influencing factor, not localization precision
- good visualization
- linearity (intensity image = O(n) of density)
- structure preservation : retain resolved, supress unresolved?
- Sampling limits the smallest resolvable detail to a size of ;2 Nd,where Nd is the mean distance between an event and its local neighbors. This is a minimum requirement ~Shannon,;2 Nd,where Nd is the mean distance between an event and its local neighbors. This is a minimum requirement ~Shannon, 1949; Heintzmann
##### Adaptive bin size histo quad tree based
- pixels are leafs of a quad/oct tree (2^D where D=dimension)
- Bin capacity N
 - Expected = N/2 for uniform (noise)
 - SNR = sqrt(N/2)
 - Setting N --> determining SNR
 - Conversely given SNR we can find N
##### Triangulation based
- Delaunay simplices size is function of density
- brightness is 1/area
- Needs smoothing to avoid distracting effect from fractal inducing effect
  - average k delaunay's of randomized
  - Gaussian intensity transition
  - jitter = we have chosen a normally distributed jitter with a width s = d, where d is average distance to neighbours
#### Related Work
##### 2D scattergram
  - position -> symbol scaled with accuracy
  - high density collides symbols
##### 2D Gaussian additive with sigma = accuracy
  - image density is signal density
##### 2D histogram
  - bin with pixel size f(precision)
  - intensity = occupance (!= ph count)
  - linear in density but better representation of SNR
  - grid introduces artifacts by rectangular square bins



#### Data
Synthetic / Real


#### Evaluation
- all except scatter are linear
- Gaussians incur a resolution loss of 1.4 (sqrt(2))
  - convolution of 2 Gaussians is Gaussian with std = sqrt(sum G1, G2)
  - since std = res
  - std = sqrt(2 res)
  - assigns too much confidence to spurious structures
- Nonuniformity measure
  - std/mean intensity on uniform data
    - want as small as possible (small std)
    - quad tree is good until plateau (needs to be tuned for SNR)
    - smoothed triangulation is good overall
- quad tree is parameter free(ish), best resolution scaling, still grid like


#### Conclusion
Introduces multiresolution adaptive parameter free methods for visualizing 2/3D SMLM data accurately with linear intensity/density values

#### Notes

#### Extra References
