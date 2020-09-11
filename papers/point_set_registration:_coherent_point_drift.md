## Point Set Registration: Coherent Point Drift

### MetaData
##### [Url](https://arxiv.org/abs/0905.2635)

##### Type
algorithm 

##### Domain
CS

##### Keywords 
Registration, correspondence, matching, alignment, rigid, non-rigid, point sets, Coherent Point Drift, CPD, Gaussian mixture model, GMM, coherence, regularization, EM algorithm, geometry, spectral

##### Cite
e.g. BibLatex
```LaTex
@article{Myronenko2009,
abstract = {Point set registration is a key component in many computer vision tasks. The goal of point set registration is to assign correspondences between two sets of points and to recover the transformation that maps one point set to the other. Multiple factors, including an unknown non-rigid spatial transformation, large dimensionality of point set, noise and outliers, make the point set registration a challenging problem. We introduce a probabilistic method, called the Coherent Point Drift (CPD) algorithm, for both rigid and non-rigid point set registration. We consider the alignment of two point sets as a probability density estimation problem. We fit the GMM centroids (representing the first point set) to the data (the second point set) by maximizing the likelihood. We force the GMM centroids to move coherently as a group to preserve the topological structure of the point sets. In the rigid case, we impose the coherence constraint by re-parametrization of GMM centroid locations with rigid parameters and derive a closed form solution of the maximization step of the EM algorithm in arbitrary dimensions. In the non-rigid case, we impose the coherence constraint by regularizing the displacement field and using the variational calculus to derive the optimal transformation. We also introduce a fast algorithm that reduces the method computation complexity to linear. We test the CPD algorithm for both rigid and non-rigid transformations in the presence of noise, outliers and missing points, where CPD shows accurate results and outperforms current state-of-the-art methods.},
archivePrefix = {arXiv},
arxivId = {arXiv:0905.2635v1},
author = {Myronenko, Andriy and Song, Xubo},
eprint = {arXiv:0905.2635v1},
file = {:home/bcardoen/Documents/Mendeley Desktop/Myronenko, Song - 2009 - Point Set Registration Coherent Point Drift.pdf:pdf},
keywords = {()},
title = {{Point Set Registration: Coherent Point Drift}},
year = {2009}
}
```
## Content
#### Research Question
(Non) Rigid Point Set Registration

__Input__: A:Nxk, B:Mxk matrices of N, M points (N!=M), k >= 2 (dimensions)

__Output__: correspondence g s.t. $(A,B) \in g$

__Key Idea__: View A as centroids of GMM, fit B to A enforcing topology constraint of A.

#### Contribution
Linear probabilistic algorithm for (non) rigid point set registration robust to noise, outliers and missing data. 

#### Method
Recap of terms:
* Rigid: Translation, Rotation, Scaling
* Non rigid: R + {Affine, Anisotropy, ...}
##### Challenges
* Outliers: points without corresponding pair
* Noise
* Dimensionality: problematic > 3

##### GMM
GMM with Gaussians + uniform to model noise, outliers.


#### Related Work
##### Rigid
* ICP : repeat: align (use PCA initial), find correspondence 
    * \+ fast
    * \- not robust, initial alignment biased
* RPM : Robust Point Matching, probabilistic, similar to EM-GMM
* Spectral Methods -- Gaussian Proximity Matrix (Gram): works well rigid, fails in non-rigid
    * Computationally expensive
    * Correspondence and transformation are factors of Gram matrix
* EM-GMM: One point set is centroid of GMM with equal isotropic covariances. E step computes probabilities, M updates transformation
    * needs extra distribution to model outliers
    * needs deterministic annealing to avoid local minima
##### Non Rigid
* ThinPlateSpline-RPM: TPS is parameterization of non-rigid transform
    * TPS D>3 does not exist
* Alignment of distributions 
* Coherence Point Drift: non rigid, regularize velocity field between point sets

 


#### Data
Synthetic (2D point sets), Stanford point sets

#### Evaluation
Error (MSE with ground truth), robustness (noise & outliers).
Proposed CPD shown to be more accurate, more robust compared with TPS-RPM. Faster approximation unstable as target is approached.


#### Conclusion
Accurate robust (non) rigid registration algorithm using GMM. 

#### Notes

#### Extra References
