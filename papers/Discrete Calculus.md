## Title
Discrete Calculus
### MetaData
##### Url

##### Type
review

##### Domain
CS

##### Keywords
discrete vector field, calculus


##### Cite
```LaTex
@article{Grady,
author = {Grady, L J and Polimeni, J R},
file = {:home/bcardoen/Downloads/grady{\_}polimeni{\_}discrete{\_}calculus.pdf:pdf},
mendeley-groups = {CREATE,graph,SRM},
title = {{Discrete Calculus}},
url = {ftp://nozdr.ru/biblio/kolxo3/Cs/CsDi/Grady L., Polimeni J. Discrete calculus.. Applied analysis on graphs for computational science (Springer, 2010)(ISBN 1849962898)(O)(371s){\_}CsDi{\_}.pdf}
}

```
## Content
#### Research Question
Discrete calculus

#### Contribution


#### Method
discrete calculus != calculus on discretized
cell complex, superset of graphs
-  The development of calculus on surfaces belongs to the classical discipline of differential geometry. The abstraction of calculus and exten-beyond three dimensions. The development of calculus on surfaces belongs to the classical discipline of differential geometry. The abstraction of calculus and exten- sion to higher dimensions is sometimes called exterior calculus or the theory of classical discipline of differential geometry. The abstraction of calculus and exten- sion to higher dimensions is sometimes called exterior calculus or the theory of differential forms
- complex network v trivial (trivial is regular graph where degree is identical)
- content extraction : data > information, examples : denoise, cluster, ranking, manifold learning
- domain in continuous space = cell complex
- 0 cell: point, 1-cell is edge, 2-cell = face
- graph is a 1-complex (has no faces)
- D is a 2-complex or 3-complex
WHAT IS A COCHAIN
- border of a cell should be a lower order cell
- Inverse of a covariance matrix is potential, precision or information matrix
- Incidence matrix: For graph, A[i,j] = 1 if j->i, 0 if !eij, -1 if i->j
- Total unimodularity: if every submatrix of A has det 0, 1, -1 then lin prog with this matrix (with int constraints) has an integer solution
- Matrix-Tree theorem: $$ \vert L_0 \vert = \vert A_0 A_0^T \vert = nr of spanning trees in graph
- Cauchy M-estimator (for estimating edges between vertices, where vertices are datapoints)
- Welsch weighting function for multivariate (multilpe independent 0-cochains):
  - $$w_{ij} = e^\{- \frac{\vert \vert s_i - s_j \vert \vert ^2}{\alpha} } $$
- Locality preserving projections : When comparing 2 vectors in k dimensions, assume n<k dimension embedding and project onto lower dimensional plane
  - uses Laplacian Eigenmaps projection
- shift invariant graph
  - if permutation of nodes leads to Laplacian being circulant (solvable by DFT)
  - circulant matrix is a matrix where R_i is an n-shift of R_j for i!=j
  - has to be regular (degree(v) = degree(u) forall u,v and u!=v)
  - regular !=> SIG
- edge weight with repulsion (u,v) and c(u) != c(v) => e(u,v) < 0, else > 0
- Joint statistics edge weight: expected correlation of data (u, v), correlation can be + -
- Mahalanobis distance for multivariate node data with known covariance matrix (sampled)
##### Filtering on graphs (chapter 5)
- node (vertex) = 0 cochain
- edge (arrow, link) = 1 cochain
- Spectral filtering
  - Eigenvectors of Laplacian : Q
  - Project data onto Q : x' = Qx
  - Filter x' to x^
  - Return to G : x'' = x^Q
- Taubin spectral filtering
  - With parameters $\mu, λ$ remove high frequency by a DFT on the normalized Laplacian
- frequency based filtering is not always valid (sometimes noise is low frequency (pink noise))
###### Manifold learning
PCA is linear
MaL is non linear
Aim: given $s_i \in R^m$ , find $f(s_i)=x_i$ s.t. $x_i \in R^n$ with $n<m$
E.g. in XY, PCA find a basis vector (line) but can't do it for a sphere
- Multi dimensional scaling:
  - Given distance matrix S
  - Construct P=−1/2 HSH with H = I - 1/n 1 1^T
  - EigVec(P) = Q Λ Q ^T
  - Set the low-dimensional coordinates as X =Q Λ^(1/2)?
  - Each col i of X is x_i, is v_i in low coord space
  - Truncate x_i for index(eigenvector | eigenvalue < \Beta)
- Isomap
  - Connect each point with its k neighbours
  - Compute all pairs shortest distances (Floyd)
  - S = shortest distance matrix

LE Algorithm
  - Spectral coordinates
  - L = Q Λ Q^T (Q is eigenvalue)
    -> x_i = columns of eigenvector matrix
T(i,j) = commute time, E[random walker from i to j to i ]

Both LE and ISOMAP require Eigv (expensive as N goes up) and not updateable

Locality preserving projections
LE + n = lin comb m

Laplacian --> Use affinity, not distance weights!!


Can be used for clustering by reducing to 1 dimension then clustering on a line, and thresholding

Why Manifold learning
- Data discovery (insight into data distribution)
- Classify on lower space
- Interpolation between objects

- Divergence
  - Sum of in/out coming edge flows
- Curl
  - Flow along cycles
#### Related Work
Place work in field

#### Data
Describe dataset (for reviews, covered literature)

#### Evaluation
Evaluation method, statistics, ...

#### Conclusion
Succinct summary

#### Notes

#### Extra References
