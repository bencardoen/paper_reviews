## Title
Deep Learning on Graphs : A Survey
### MetaData
##### Url
arXiv:1710.09599
##### Type
review

##### Domain
CS

##### Keywords
graphs, dnn, dl, machine learning, deep learning


##### Cite

```LaTex

```
## Content
#### Research Question
Review on GNN

#### Contribution
* GNN
    * s_i = sum (si, sj, Fvi, Fvj, Feij) // recursive
    * yi = O(si, Fvi)
    * F's are learned
    * Constrained by requirement for unique solution of F
    * F should be contraction map
        * d(f(x),f(y)) <= k d(x,y) in metric space M,d
* Gated Graph Sequence Neural Networks (GGS-NNs)
    * Gated Recurrent Units
    * sit = (1-zit) * sit-1 + zit sit~ (candidate)
* GCNN
    * Convolution defined on Laplacian (L = D-A)
    * defined output as
    * u' = QΘQTu
    * Θ = Θ(Λ) ∈ RN×N is a diagonal matrix of learnable filters with Lamdba eigenvalues of L
    * Spectral domain filters may not exist in spatial domain
    * expensive, fixed to specific graph size
    * Chebnet uses Chebyshev polynomials to map spectral to spatial, and is faster
    * Neural FPs for per degree filters, works well for small graphs, may not scale
    * PATCHYSAN : convert to 1D CNN using l<k nearest neighbours
    * Difusion CNN:
        * H' = p(Pk H TH)
        * Pk is kth transition matrix
        * H is previous layer
        * K is preset value
        * TH is diagonal matrix of learnable parameters
        * Only Pk is graph specific, but O(N^2 K)
    * Readout (GCNN) output node focused tasks, not graph focused tasks, readout method should be adapted to be e.g. order invariant.
* Hierarchical clustering
    * Sampling to accelerate
    * Edge features work separately
    *
* GAE
    * SAE : deep layer multiperceptron outperforms k means
    * PPMI: positive pointwise mutual information
        PMI : log { p(x|y) } / {p(x)p(y)}
* VAE
    * Wasserstein metric https://en.wikipedia.org/wiki/Wasserstein_metric
    * Wasserstein is metric, KL is not
* GRNN
    * You et al : Node RNN, Edge RNN to generate graph
    * DGNN uses LSTM for GNN over time
    * DGCN uses spatio and temporal aspects
    * GCPN RL agent generating graph
    * MolGan

* Future directions
    * Interpretability, freedom, structure of graphs
    

#### Method


#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
