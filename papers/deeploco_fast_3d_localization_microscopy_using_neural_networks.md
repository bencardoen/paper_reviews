## Title
DeepLoco: Fast 3D Localization Microscopy Using Neural Networks
### MetaData
##### Url
[url](https://www.biorxiv.org/content/early/2018/02/16/267096)
##### Type
review, (novel) method, (new) dataset, analysis, ... 

##### Domain
Single line of domains separated by comma.

E.g. Biology, CS, Mathematics, ...

##### Keywords 
key1, key2, key3, ...

A single line of comma separated keywords. These are machine parsed to create a keyword tree where a paper is placed into folders named by their keyword.
A single paper can appear in multiple folders (never copied, only the symbolic link will appear.)

Example:
__computer graphics, networks, graph analysis__

 


##### Cite
e.g. BibLatex
```LaTex
@article{Boyd2018,
abstract = {Single-molecule localization super-resolution microscopy (SMLM) techniques like STORM and PALM have transformed cellular microscopy by substantially increasing spatial resolution. In this paper we introduce a new algorithm for a critical part of the SMLM process: estimating the number and locations of the fluorophores in a single frame. Our algorithm can analyze a 20000-frame experimental 3D SMLM dataset in about one second - substantially faster than real-time and existing algorithms. Our approach is straightforward but very different from existing algorithms: we train a neural network to minimize the Bayes' risk under a generative model for single SMLM frames. The neural network maps a frame directly to a collection of fluorophore locations, which we compare to the ground truth using a novel loss function. While training the neural network takes several hours, it only has to be done once for a given experimental setup. After training, localizing fluorophores in new images is extremely fast - orders of magnitude faster than existing algorithms. Faster recovery opens the door to real-time calibration and accelerated acquisition, and future work could tackle more complicated optical systems and more realistic simulators.},
author = {Boyd, Nicholas and Jonas, Eric and Babcock, Hazen P and Recht, Benjamin},
doi = {10.1101/267096},
file = {:home/bcardoen/Documents/Mendeley Desktop/Boyd et al. - 2018 - DeepLoco Fast 3D Localization Microscopy Using Neural Networks(3).pdf:pdf},
journal = {bioRxiv},
mendeley-groups = {SRM},
month = {feb},
pages = {267096},
publisher = {Cold Spring Harbor Laboratory},
title = {{DeepLoco: Fast 3D Localization Microscopy Using Neural Networks}},
url = {https://www.biorxiv.org/content/early/2018/02/16/267096},
year = {2018}
}

```
## Content
#### Research Question
smlm photon stack to localization

#### Contribution
DL + Bayes

#### Method
Metric: MSQ of image to image comparison

#### Related Work


#### Data
Describe dataset (for reviews, covered literature)

#### Evaluation
Evaluation method, statistics, ...

#### Conclusion
Weakness is fragility

Compares to 2016 state of art, so it's outdated.

Tested on benchmark, simulators without noise.

Highly sensitive to SNR
#### Notes

#### Extra References
