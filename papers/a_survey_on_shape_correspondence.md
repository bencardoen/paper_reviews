## A Survey on Shape Correspondence

### MetaData
##### Url
https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-8659.2011.01884.x

##### Type
review 


#### Domain
CS
##### Keywords 
shape, geometry, computer graphics

##### Cite
e.g. BibLatex
```LaTeX
@article{VanKaick,
abstract = {We review methods designed to compute correspondences between geometric shapes represented by triangle meshes, contours, or point sets. This survey is motivated in part by recent developments in space-time registration, where one seeks a correspondence between non-rigid and time-varying surfaces, and semantic shape analysis, which underlines a recent trend to incorporate shape understanding into the analysis pipeline. Establishing a meaningful correspondence between shapes is often difficult since it generally requires an understanding of the structure of the shapes at both the local and global levels, and sometimes the functionality of the shape parts as well. Despite its inherent complexity, shape correspondence is a recurrent problem and an essential component of numerous geometry processing applications. In this survey, we discuss the different forms of the correspondence problem and review the main solution methods, aided by several classification criteria arising from the problem definition. The main categories of classification are defined in terms of the input and output representation, objective function, and solution approach. We conclude the survey by discussing open problems and future perspectives.},
author = {{Van Kaick}, Oliver and Zhang, Hao and Hamarneh, Ghassan and Cohen-Or, Daniel},
pages = {1--24},
title = {{A Survey on Shape Correspondence}},
volume = {xx}
}
```

## Content
#### 0. Research Question
###### 0.0 Definition
Shape Correspondence:
Let S = {S_i | i : 1..N} be a set of input shapes. Define relation R between elements of the sets.

$(p, q) \in R | p \in S_i \land q \in S_j \land i \neq j$

Shape is composed of elements (points, features), seek correspondence between elements.

#### Contribution
Overview and classification of the field.

#### Method
##### Query/Retrieval versus Correspondence
Given q, find most similar shapes (query), correspondence finds exact matches.
##### Tasks
* Full versus partial : similar to graph-subgraph matching
* Sparse vs Dense : e.g. only look at gradient points vs all points
* Grouped: R(p,q,r,z,...) allows for detection of common features
##### Approaches

![overview](../img/correspondence_methods.png)

###### Transformations
* Rigid Transformation: preserves point wise distances (rot, refl, trans)
* Conformal (angle preserving)
* Mobius-Homograph: RT & C
* Non Linear

###### Objective Functions
O(correspondence) --> R

###### Similarity based
O(p, q, R) = Sim(p, q, R) + a Distor(p,q, R)

p, q shapes, R correspondence, a weight of distortion (transformation).

Distortion typical = Distance (pointwise): euclidean, geodesic

###### Rigid alignment
* Largest Common Pointset
* Chamfer (one-way)
* Iterated Closest Point (ICP) uses Chamfer. Additional rotation terms etc are optional.
###### Non-Rigid alignment
* Penalize quantified loss of semantics by transformation


#### Related Work
N/A

#### Data
N/A

#### Evaluation
N/A

#### Conclusion
Succinct summary

#### Notes
Rigid Transformation: preserves point wise distances (rot, refl, trans)

#### Extra References and links
1. [Quadratic Programming](https://en.wikipedia.org/wiki/Quadratic_programming)

