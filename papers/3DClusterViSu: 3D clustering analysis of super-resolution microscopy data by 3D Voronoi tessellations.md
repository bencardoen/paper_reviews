## Title
3DClusterViSu: 3D clustering analysis of super-resolution microscopy data by 3D Voronoi tessellations
### MetaData
##### Url
https://academic.oup.com/bioinformatics/article/34/17/3004/4960045
##### Type
method

##### Domain
CS, Biology

##### Keywords
smlm, superresolution, voronoi, 3d, analysis, point clouds, localization analysis

##### Cite
e.g. BibLatex
```LaTex
@article{Andronov2018,
abstract = {Single-molecule localization microscopy (SMLM) can play an important role in integrated structural biology approaches for example at the interface of cryo electron microscopy (cryo-EM), X-ray crystallography, NMR and fluorescence imaging to identify, localize and determine the 3D structure of cellular structures. While many tools exist for the 3D analysis and visualisation of crystal or cryo-EM structures little exists for 3D SMLM data which can provide fascinating insights but are particularly challenging to analyze in three dimensions especially in a dense cellular context. We developed 3DClusterViSu, a method based on 3D Voronoi tessellations that allows local density estimation, segmentation {\&} quantification of 3D SMLM data and visualization of protein clusters within a 3D tool. We show its robust performance on microtubules and histone proteins H2B and CENP-A with distinct spatial distributions. 3DClusterViSu will favor multi-scale and multi-resolution synergies to allow integrating molecular and cellular levels in the analysis of macromolecular complexes.},
author = {Andronov, Leonid and Michalon, Jonathan and Ouararhni, Khalid and Orlov, Igor and Hamiche, Ali and Vonesch, Jean Luc and Klaholz, Bruno P.},
doi = {10.1093/bioinformatics/bty200},
file = {:home/bcardoen/Downloads/bty200.pdf:pdf},
issn = {14602059},
journal = {Bioinformatics},
mendeley-groups = {doublelabelling,SRM},
number = {17},
pages = {3004--3012},
title = {{3DClusterViSu: 3D clustering analysis of super-resolution microscopy data by 3D Voronoi tessellations}},
volume = {34},
year = {2018}
}

```
## Content
#### Research Question
3D SMLM visualization and analysis tools are few (compared to EM)
Why 3D?
2D overlapping cluster (1) is in fact multiple 3D

#### Contribution
local density estimation, segmentation and quantification of 3D SMLM data and visualization of protein clusters within a 3D tool

#### Method
- Leica 3D GSD dSTORM
- Reduction of number of points by 'averaging the coordinates of consecutive events within a radius of 50 nm'
- drift correction
  - split into subsets (consecutive)
  - 20nm heatmap
  - detect shift between images
  - detect lateral drift in XY, average YZ/XZ, subtract
- ROI selection to remove edge effect (infinite Voronoi at edge)
- isotropy correction
  - Gaussian density is reversed by multiplying with factor inverse of Gaussian at Z = k
- Removal of sparse clusters either by filtering, or first rank density (<mean density, or averaged first rank)
- Autotuned, so no optimization
- Run uniform noise MC random noise experiment to come up with a mean and confidence values of volume
- If the experimental distribution is outside that CI, then it is a cluster


#### Related Work
2D alternatives are
-SRTesseler
-Bayesian Clustering
-ClusterViSu -- Voronoi
3D
-DBSCAN
-Getis and Franklin’s local point pattern analysis

#### Data
- Uniform random X/Y with Gaussian Z
- "The distributions were generated for 50 different random sets of points, the boundaries of the 95% confidence envelopes were determined as<n> 6 1.96?r for each bin of the histogram, where<n>is the average number of cells within the range of the bin and r is the standard deviation of n, calculated from the 50 random datasets. The segmentation thresh- old, defined as the abscissa of the first intersection between the curves of the experimental and the mean value of the randomized distributions was determined from the two points around the inter- section in the linear approximation."
- "2D projec-tions (Fig. 3E–F) were built as histogram images with the bin size of 20 nm. The signal-to-noise ratios were calculated as <I>/rI, where <I> is the mean value of the non-zero pixels and rI is the standard deviation of all pixel values, yielding <I>/rI ¼ 1.6 (Fig. 3E) and <I>/rI ¼ 2.2 (Fig. 3F). "
- "randomly distributed points inside spheres with a radius of 30 nm. The positions of clusters and of background points were distributed randomly in the FOV, with the following constraints: 1) distance from the centers of the clusters to the borders?75 nm; 2) distance between the centers of the clus- ters?150 nm. The borders of the clusters were smoothened such that the density of molecules at the distance r from the center of the cluster was modulated with the function p(r) ¼ 1=2(1þerf(4?(r0-r) /r0)), where r0 ¼ 30 nm and erf(x) is the Gauss error function."

#### Evaluation
- Time : 6 h to segment a large experimental dataset
with a volume of ?200 mm3 that contains 106 localizations

#### Conclusion
A full package approach for 3D segmentation of SMLM localizations, fast, autotuned, validated on random synthetic data.

#### Notes

#### Extra References
