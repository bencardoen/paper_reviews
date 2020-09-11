## Title
Beyond co-localization: Inferring spatial interactions between sub-cellular structures from microscopy images
### MetaData
##### Url
10.1186/1471-2105-11-372
##### Type
method

##### Domain
Biology, CS, Statistics

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@article{Helmuth2010,
abstract = {BACKGROUND: Sub-cellular structures interact in numerous direct and indirect ways in order to fulfill cellular functions. While direct molecular interactions crucially depend on spatial proximity, other interactions typically result in spatial correlations between the interacting structures. Such correlations are the target of microscopy-based co-localization analysis, which can provide hints of potential interactions. Two complementary approaches to co-localization analysis can be distinguished: intensity correlation methods capitalize on pattern discovery, whereas object-based methods emphasize detection power. RESULTS: We first reinvestigate the classical co-localization measure in the context of spatial point pattern analysis. This allows us to unravel the set of implicit assumptions inherent to this measure and to identify potential confounding factors commonly ignored. We generalize object-based co-localization analysis to a statistical framework involving spatial point processes. In this framework, interactions are understood as position co-dependencies in the observed localization patterns. The framework is based on a model of effective pairwise interaction potentials and the specification of a null hypothesis for the expected pattern in the absence of interaction. Inferred interaction potentials thus reflect all significant effects that are not explained by the null hypothesis. Our model enables the use of a wealth of well-known statistical methods for analyzing experimental data, as demonstrated on synthetic data and in a case study considering virus entry into live cells. We show that the classical co-localization measure typically under-exploits the information contained in our data. CONCLUSIONS: We establish a connection between co-localization and spatial interaction of sub-cellular structures by formulating the object-based interaction analysis problem in a spatial statistics framework based on nearest-neighbor distance distributions. We provide generic procedures for inferring interaction strengths and quantifying their relative statistical significance from sets of discrete objects as provided by image analysis methods. Within our framework, an interaction potential can either refer to a phenomenological or a mechanistic model of a physico-chemical interaction process. This increased flexibility in designing and testing different hypothetical interaction models can be used to quantify the parameters of a specific interaction model or may catalyze the discovery of functional relations.},
author = {Helmuth, Jo A. and Paul, Gr{\'{e}}gory and Sbalzarini, Ivo F.},
doi = {10.1186/1471-2105-11-372},
file = {:home/bcardoen/Downloads/1471-2105-11-372.pdf:pdf},
issn = {14712105},
journal = {BMC Bioinformatics},
title = {{Beyond co-localization: Inferring spatial interactions between sub-cellular structures from microscopy images}},
volume = {11},
year = {2010}
}


```
## Content
#### Research Question
Two complementary approaches to co- localization analysis can be distinguished: intensity correlation methods capitalize on pattern discovery, whereas object-based methods emphasize detection power.
A general biological principle states that cellular func-tion results from the combined interactions of sub-cellu-lar structures in space and time.

#### Contribution
Summarized contribution(s)

#### Method
##### Prelude
- #interaction as the collection of all effects that cause significant (above the level predicted by a null hypothesis)
correlations in the positions of the participating objects.
- Direct/indirect approaches
  - Direct: signal if in contact (single channel)
  - Indirect : colocalize signal
- k structures interact => spatial distributions are correlated
- correlation !=> structure interaction
  - Reasons
    - Third (hidden) interaction causitive factor
    - Accidental correlation
    - non linear correlation
  - *Need for inference of interaction*
- Types
  - Intensity correlation --> pattern discovery
    - Interpretation in intensity space (blurring, noise, linearity, ...)
  - object based methods --> detection power
    - geometric space (counting overlap, ...), intuitive
    - distance threshold approaches

##### Method
- binary Gibbs process with fixed number of objects
- pair wise interaction potential (energy level of 2 interacting objects)
- Boltzmann distribution p(X,Y) = exp ^ {-sum_n sum_m phi(x_i, y_i)}
  - lower energy state has higher probability
  - assumption of independence of objects in X,Y
  - The Boltzmann distribution is a probability distribution that gives the probability of a certain state as a function of that state's energy and temperature of the system to which the distribution is applied.
  - p(state i ) = \frac{\exp{-ei/kt}}{\sum_j \exp{-en_j/kt}}
- Nearest neighbor adoption
  - ϕ(x_i, y_i) = (y_i is NN of x_i) ? 𝛷(d_i) : 0
  - cell context, X is source, Y is target
  - p(X| omega, Y) = \mult_i^N \exp{-ϕ(d_i)}
  - \phi(d) = ϵ f ({d-t}/σ)
    - \epsilon : strength
    - f = shape
    - t shift along distance axis
    - sigma defines scale


#### Related Work
- Nearest neighbour interaction function
  - $$ C^t = 1/N \sum 1(d_i < t)  $$ = p(d) (at N-> infty)
  - rotation and translation invariant (distance)
  - binary
  - interpretation difficult (C>0) != interaction due to confounding factors (cellular context)
  - non zero probability of observing di
  - relative frequency of possible distances
    - q(d) = lim_{\delta d \rightarrow 0} P( d_i \in [d, d+\delta d] | no interaction, Y) / \delta d
    - (state density
    - random positions / clustered positions
      - tight clusterings leads to long distances only, or exponential distributed distances
      - C^t is not sufficient to distinguish confounding factor (context) from interaction
  - interaction should be defined as a base level deviation of model expectation in absence of interaction
  - H0: no interaction, p(d) = q(d)
  - H1 if divergence from H0


#### Data
Synthetic (uniform shapes) in confocal 3D with real viral data

#### Evaluation
Evaluation method, statistics, ...

#### Conclusion
Object based interaction models require a quantification/differentiation with respect to an expected level of interaction to determine actual interaction. More general models follow the complexity theorem (higher/general can be less decided upon). Statistical inference is required to quantify interaction from the model.  Differences with SRM : object to object (requires pre clustering). The cell context has to be quantified/incorporated as a baseline to differentiate (H0) and a computation of Ct/C0 with power analysis is needed. The Gibbs model where interaction is an energy potential P(state i) = exp(i) / sum exp(j)

#### Notes

#### Extra References
