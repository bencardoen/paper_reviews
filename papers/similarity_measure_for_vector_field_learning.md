## Similarity Measure for Vector Field Learning

### MetaData
##### [Url](http://link.springer.com/10.1007/11759966_65)

##### Type
algorithm, metric 

##### Domain
CS

##### Keywords 
vector field, measure, similarity, machine learning, vector, euclidean, manifold

 


##### Cite
e.g. BibLatex
```LaTex
@incollection{Li2006,
author = {Li, Hongyu and Shen, I-Fan},
doi = {10.1007/11759966_65},
file = {:home/bcardoen/Documents/Mendeley Desktop/Similarity{\_}Measure{\_}for{\_}Vector{\_}Field{\_}Learning.pdf:pdf;:home/bcardoen/Documents/Mendeley Desktop/Li, Shen - 2006 - Similarity Measure for Vector Field Learning.pdf:pdf},
mendeley-groups = {graph,SRM},
pages = {436--441},
publisher = {Springer, Berlin, Heidelberg},
title = {{Similarity Measure for Vector Field Learning}},
url = {http://link.springer.com/10.1007/11759966{\_}65},
year = {2006}
}


```
## Content
#### Research Question
Define a similarity measure that compares vectors outside of euclidean space.

#### Contribution
Similarity based a linear of distance, angle, magnitude.

Feature extraction using Locally Linear Embedding



#### Method
Similarity of points using Euclidean Gaussian Kernel

s(p_i, p_j) = exp(-(d(p_i, p_j)/sigma_1^2)

__Input__ : 
v_i, v_j

__Output__: 
scalar similarity

s(v_i, v_j) = \alpha e^{-d(p_i, p_j)} \beta e^{1-a(p_i, p_j)} + \gamma e^{-m(p_i, p_j)}

a+b+c = 1

a(v_i, v_j) = angular difference

m(v_i, v_j) = magnitudal difference 
  

#### Related Work

#### Data
Synthetic 1D manifolds

#### Evaluation
Visual

#### Conclusion

#### Notes
* [Manifold](http://mathworld.wolfram.com/Manifold.html): A manifold is a topological space that is locally Euclidean (i.e., around every point, there is a neighborhood that is topologically the same as the open unit ball in R^n). To illustrate this idea, consider the ancient belief that the Earth was flat as contrasted with the modern evidence that it is round. The discrepancy arises essentially from the fact that on the small scales that we see, the Earth does indeed look flat. In general, any object that is nearly "flat" on small scales is a manifold, and so manifolds constitute a generalization of objects we could live on in which we would encounter the round/flat Earth problem, as first codified by Poincaré.




#### Extra References
