## Measuring the similarity of vector fields using global distributions

### MetaData
##### [URL](http://link.springer.com/10.1007/978-3-540-89689-0_23)

##### Type
metric, measure, algorithms 

##### Domain
CS

##### Keywords 
vector, vector field, manifold, distribution, geometry, matching, distance, similarity
 


##### Cite
e.g. BibLatex
```LaTex
@incollection{Dinh2008,
author = {Dinh, H. Quynh and Xu, Liefei},
booktitle = {Proceedings of the 2008 Joint IAPR International Workshop on Structural, Syntactic, and Statistical Pattern Recognition},
doi = {10.1007/978-3-540-89689-0_23},
file = {:home/bcardoen/Documents/Mendeley Desktop/Dinh-Xu2008{\_}Chapter{\_}MeasuringTheSimilarityOfVector (1).pdf:pdf},
isbn = {978-3-540-89688-3},
keywords = {geometric histogram,shape distribution,vector field matching},
mendeley-groups = {geometry,Machine learning},
pages = {187--196},
publisher = {Springer-Verlag},
title = {{Measuring the Similarity of Vector Fields Using Global Distributions}},
url = {http://link.springer.com/10.1007/978-3-540-89689-0{\_}23},
year = {2008}
}
```
## Content
#### Research Question
How do you compare 2 vector fields?

#### Contribution
Rotationally invariant geometric distribution based similarity measure to compare difference between vector fields.

#### Method

__Input__: Vector field pair

__Output__ : Scalar distance / similarity

__Method__:
Create k-D histograms, compute distance using Xi square.

Dimensions:
* Streamlines: uniformly (to prevent density clusters) distribute points and let them follow vectors
Record curvature on streamline (vectors on streamline)
* Vector dot product and distance of origins: Dot product to normal vectors


#### Related Work
Vector field analysis depends on eigenanalysis of Jacobian to find critical points (saddle, focus, center, ..)
Computationally expensive. Singularities may not exist.

#### Data
Synthetic and real (flow in combustion engine)

#### Evaluation


#### Conclusion
Rotational invariant distribution matching for vector field analysis.

#### Notes

#### Extra References
