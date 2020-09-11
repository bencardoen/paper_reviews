## Title
Review of Causal Discovery Methods Based on Graphical Models
### MetaData
##### Url
https://www.frontiersin.org/articles/10.3389/fgene.2019.00524/full

##### Type
review

##### Domain
Statistics, Mathematics

##### Keywords
causality, statistics, graphical model



##### Cite
e.g. BibLatex
```LaTex

@article{glymourReviewCausalDiscovery2019,
  title = {Review of {{Causal Discovery Methods Based}} on {{Graphical Models}}},
  author = {Glymour, Clark and Zhang, Kun and Spirtes, Peter},
  date = {2019},
  journaltitle = {Frontiers in Genetics},
  shortjournal = {Front. Genet.},
  volume = {10},
  publisher = {{Frontiers}},
  issn = {1664-8021},
  doi = {10.3389/fgene.2019.00524},
  url = {https://www.frontiersin.org/articles/10.3389/fgene.2019.00524/full},
  urldate = {2020-09-07},
  abstract = {A fundamental task in various disciplines of science, including biology, is to find underlying causal relations and make use of them. Causal relations can be seen if interventions are properly applied; however, in many cases they are difficult or even impossible to conduct. It is then necessary to discover causal relations by analyzing statistical properties of purely observational data, which is known as causal discovery or causal structure search. This paper aims to give a introduction to and a brief review of the computational methods for causal discovery that were developed in the past three decades, including constraint-based and score-based methods and those based on functional causal models, supplemented by some illustrations and applications.},
  file = {/home/bcardoen/Zotero/storage/YAAJNAMB/Glymour et al. - 2019 - Review of Causal Discovery Methods Based on Graphi.pdf},
  keywords = {causal,causal discovery,causality,Conditional independence,Directed graphical causal models,graphs,non-Gaussian distribution,Non-linear models,Statistical independence,statistics,Structural Equation Models},
  langid = {english}
}

```
## Content
#### Research Question
Automated construction of graphical models (directed, acyclic) of causality between random variables.

#### Contribution
Reveal causal information from purely observational or experimental data.

#### Definitions
##### Causality
Let X, Y be random variables.
* Necessary causality
  * $x \rightarrow_{N} y$
  * If y, then x must have occurred
  * X can occur without y
  * $y \Rightarrow x$
* Sufficient causality
  * $x \rightarrow_{S} y$
  * $x \Rightarrow y$
  * If x, then y. However, other causes can cause y, therefore y does not require y.
* Necessary and sufficient
  * $x \Leftrightarrow y$
* Contributory cause
  * x is a set of causes that together causes y. x does not need to be necessary nor sufficient
* Conditional vs causality
  * Causality requires temporal order (X occurs before or at same time as Y)
* Probabilistic causation
  * $x \rightarrow y$ , if there is some y where x is not present, then causality does not hold (x=war, y=deaths)
  * More nuanced models P[A|B] > P[A], the presence of B increases likelihood of A

#### Approaches
##### Equivalence Class Based methods (find EQ)
* PC (Spirtes, 2000)
  * Assumes no confounder
* Fast Causal Inference (Spirtes, 2000)
  * FCI works in presence of confounder
* Greedy Equivalence Search
##### Functional Causal Model (GCM)
* $Y=f(X,E)$ and X, E independent
* This allows detection of causality, because independence of noise (E) only holds for X, not Y
* Cover linear non Guassian and non-linear models
##### Directed Graphical Causal Model
* Given variables $X_i$,
* **edge** $X_i \rightarrow X_j$, if $X_k, k \neq i,j$ are kept fixed, $\exists X_i $ $cov(X_i, X_j) > 0$.
* joint probability distribution over the possible values of all the variables
* DGCM is superset of regression, SEM, factor models, ARM time series models, latent class,
* Do not require initial condition in contrast to partial differential equations
* Constraint: X is **d-separated**, then X is conditionally independent in distribution (similar to Markov, where independence on non-parent variables)
* Graphs with same **d-separated** properties are called **Markov-equivalent (ME)**, $\mathrm{G}=\{ ME(G_i, G_j) | \forall G_i, G_j \in \mathrm{G}\}$, then $\mathrm{G}$ is a **Markov Equivalence Class**, if this assumption exists: **Causal Markov Assumption**
* **path** <$X_i$...> , $\exists X_i \rightarrow X_j$ (or vice versa), directed when there is 1 direction
* **collider** : path with $X_i \rightarrow X_{i+1} \leftarrow X_{i+2}$, $X_{i+1}$ is a common effect
* **Conditional Faithfullness Assumption** : there exists no conditional indepence relations other than encoded by the graph
* Output is a matrix A of NxN ($\vert X  \vert$=N), where A[i,j] = {**p**arent (i$ \rightarrow $ j), **u**known (not known to be absent), **c**onfounded}
#### Challenges
* causality in time series
* measure error (disturbances)
* variabes can be ordinal, categorical, continuous, ...
* missing values
* heterogeneity
* selection bias

#### Differences with statistical estimation
* Statistical estimation has several desired properties:
  * Statistical consistency : under sampling assumptions estimates converge to true value
  * uniform convergence: probabilistic bounds on errors at finite sample sizes
* GCM
  * Pointwise consistency: no finite sample error probs or confidence intervals

#### Types of GVM algorithms
* Finds the MECs that fit most closely to the conditional independence of relations in the population
* Estimate the (conditional) (in) dependencies on independent noise, and use this to construct graphical model



#### Related Work
* Path analysis https://en.wikipedia.org/wiki/Path_analysis_(statistics)
* Structural Equation modeling https://en.wikipedia.org/wiki/Structural_equation_model
* Granger causality (is 1 time series forecasting another) https://en.wikipedia.org/wiki/Granger_causality

#### Data
Describe dataset (for reviews, covered literature)

#### Evaluation
Evaluation method, statistics, ...

#### Conclusion
Succinct summary

#### Notes

#### Extra References
