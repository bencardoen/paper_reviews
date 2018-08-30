## Title

Deep-STORM: super-resolution single-molecule microscopy by deep learning

### MetaData
##### Url
[https://arxiv.org/abs/1801.09631](https://arxiv.org/abs/1801.09631)
##### Type
method

##### Domain
CS, Optics, Chemistry, Biology

##### Keywords 
deep learning, smlm, microscopy, super-resolution

##### Cite
e.g. BibLatex
```LaTex
@article{Nehme2018,
abstract = {We present an ultra-fast, precise, parameter-free method, which we term Deep-STORM, for obtaining super-resolution images from stochastically-blinking emitters, such as fluorescent molecules used for localization microscopy. Deep-STORM uses a deep convolutional neural network that can be trained on simulated data or experimental measurements, both of which are demonstrated. The method achieves state-of-the-art resolution under challenging signal-to-noise conditions and high emitter densities, and is significantly faster than existing approaches. Additionally, no prior information on the shape of the underlying structure is required, making the method applicable to any blinking data-set. We validate our approach by super-resolution image reconstruction of simulated and experimentally obtained data.},
archivePrefix = {arXiv},
arxivId = {1801.09631},
author = {Nehme, Elias and Weiss, Lucien E. and Michaeli, Tomer and Shechtman, Yoav},
doi = {10.1364/OPTICA.5.000458},
eprint = {1801.09631},
file = {:home/bcardoen/Documents/Mendeley Desktop/1801.09631.pdf:pdf},
issn = {2334-2536},
mendeley-groups = {deep learning,SRM},
title = {{Deep-STORM: super-resolution single-molecule microscopy by deep learning}},
year = {2018}
}
```
## Content
#### Research Question
Photon matrix to localizations / image in smlm.

#### Contribution
Deep learning (enc-dec) approach to problem, input is photon matrix, claimed parameter free and fast.

#### Method
End-Dec network, requires settings of PSF model and camera.
Loss function is MSE with Gaussian kernel + 1 norm of locations (forcing centering?)

Guassian kernel of sigma 1 (pixel), 2 hrs of training.

Resolution is 

#### Related Work
Celo, Falcon (computational), lower speed, better accuracy.

#### Data
ThunderStorm ImageJ, 208x208 pixels random low density (500 points)
Microtubules

#### Evaluation
Synthetic (tubules : straight lines)

SNR : 1000 photons to 10 background (??)


#### Conclusion
Weak point: need model, PSF, camera, still model based approach.
Resolution is 9 emitters per micrometer = 40nm!!

#### Notes

#### Extra References
