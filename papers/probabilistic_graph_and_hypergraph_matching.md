## Probabilistic graph and hypergraph matching.

### MetaData
##### [Url](http://ieeexplore.ieee.org/document/4587500/)

##### Type
algorithm 

##### Domain
CS

##### Keywords 
graph theory, graph analysis, hypergraph, matching, approximate, probabilistic

 


##### Cite
e.g. BibLatex
```LaTex
@inproceedings{Zass2008,
author = {Zass, Ron and Shashua, Amnon},
booktitle = {2008 IEEE Conference on Computer Vision and Pattern Recognition},
doi = {10.1109/CVPR.2008.4587500},
file = {:home/bcardoen/Documents/Mendeley Desktop/matching-cvpr08 (1).pdf:pdf},
isbn = {978-1-4244-2242-5},
mendeley-groups = {SRM},
month = {jun},
pages = {1--8},
publisher = {IEEE},
title = {{Probabilistic graph and hypergraph matching}},
url = {http://ieeexplore.ieee.org/document/4587500/},
year = {2008}
}
```
## Content
#### Research Question
Find a matching between vertices by hypergraph construction.


#### Contribution
Fast accurate hypergraph matching with edge degree identical.

Algebraic relation between edge similarity matrix and vertex similarity matrix.



#### Method
Given G, G'.

__Input__ : S(e, e') = Pr(m(e)) = e'

__Output__: X(v, v') = Pr(m(v)=v')

Soft matching iff X is doubly stochastic:

sum(X[:,i]) = 1 forall i, sum(X[i,:])= 1 for all i

If complete graph is impossible/infeasible, selected edges may help.
  

#### Related Work
Place work in field

#### Data
Synthetic:
* 25 points in 2D, G' is rotated perturbed. Distance mean normalized to 1. Point to point matching needed. 
Complete graph, with edge as euclidean distance. S[e,e'] = exp(-|d-d'|)

#### Evaluation

#### Conclusion
Effective method for unbalanced data, yet requires complete graph.

Sampling scheme uses O(VV' z^2)

Improved performance to spectral graph matching 

#### Notes
Hypergraph is a graph where an edge links V^d vertices.

#### Extra References
