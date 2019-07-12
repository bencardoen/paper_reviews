## Title
Classic Works of the Dempster-Shafer Theory of Belief Functions: An Introduction∗
### MetaData
##### Url
ISBN 9783540343561
##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
@book{Yager2008,
abstract = {},
author = {Yager, Ronald R and Liu, Liping},
booktitle = {Classic Works of the Dempster-Shafer Theory of Belief Functions},
file = {:home/bcardoen/Downloads/2008{\_}Book{\_}ClassicWorksOfTheDempster-Shaf.pdf:pdf},
isbn = {9783540343561},
pages = {I--XIX},
title = {{Classic Works of the Dempster--Shafer Theory of Belief Functions: Front Matter}},
year = {2008}
}

```
## Content
#### Research Question
Review of Belief functions

#### Contribution


#### Method
- Given question of interest, let $$\Theta$$ be the set of possible answers, 'set of discernment'
- Function $$ Bel(2^\Theta) \rightarrow [0,1]$$
  - iff
    - Bel(∅) = 0
    - Bel(\Theta) = 1
      - Let $$ A_{1..n} \subset \Theta $$
      - $$ Bel(\bigcup A_i) \geq \sum_{I \subset {1..n}, \neq ∅} (-1)^{|I|+1} Bel(\bigcap A_i)
  - for n =2 and $$\bigcap A_i = \emptyset$$ this is the probablity theorem, probability functions are belief functions but not the inverse
  - Bel(A) != additive
    - Counterexample, crime committed with 100 candidates
      - 1 candidate looks flustered when questions
      - Bel({guilty}) < 1 , becuase other reasons for flustered may exist
      - Bel({innocent}) = 0, because innocence is not proven if flustered is caused by crime
      - Bel({guilty, innocent}) =1 , so not additive
    - belief is divided into 1+ basic p numbers m(A), focal elements
    - $$ \sum {m(A) \vert A \subseteq \Theta} = 1 $$
      - m(A) is indivisible
    - $$ Bel(A)= \sum {m(B) | B \subseteq A} $$
    - $$m(A) = \sum {(-1)^{|vert A -B \vert} Bel(B) \vert B \subset A}
    - Recursive : m(∅) =0, m(A) = Bel(A) - $$ \sum {m(B)\vert B \subset A}
    - $$Pl(A) = 1 - Bel(\neg {A})$$
      - Plausibility
      - $$Pl(A) = \sum {m(B) \vert A \cap B \neq ∅ }$$
    - Bel(A) <= Pl(A)
    - A, B where B ⊂ A
      - B stronger proposition than A
      - B requires stronger evidence in support
      - evidence supporting A does not necessarily support A
    - Rule of combination
      - m1, m2 independent evidence mass function
        - intersection of m1, m2 become new focal element
      - $$ m(A) = \frac{\sum {m1(B)m2(C)} \vert B \cap C = A} {\sum {m1(B) m2(C) \vert B \cup C \neq \emptyset}}
    - Weight of conflict
      $$ W = \log(\frac{1}{\sum {m1(B) m2(C) \vert B \cup C \neq \emptyset}}) $$
    - $$ W \neq \infty \Leftrightarrow B,C combinable $$
    - For any two propositions A,B and B \subset A
      - Pl(A) >= Pl(B)
      - Bel(A) >= Pl(B)
  - Types of belief function
    - Vacuous belief function = full ignorance, evidence does not support or inform
      - Θ is only focal element
    - Bayesian belief function = assign p to each singleton in Θ
      - Bel(A) = Pl(A)
      - Bel(AUB) = Bel(A) + Bel(B) (if A isec B = empty)
    - simple support function represents homogeneous evidence provides support for exactly 1 proposition (1 proper subset of \Theta) (so 2 focal elements, S and Θ)
    - separable support function
      - orthogonal sum of SSF
      - if A,B focal and A isec B neq 0, then A isec B is focal element
      - example
        - frame = {r, n, s}
        - m({r,n}) = 0.2
        - m({s,n}) = 0.5
        - m(\Theta) = 0.3
        - m(AUBUC) = m(frame) = focal element
        - rn \isec sn = n, n is not focal element, so n SSF
    - How to encode ignorance
      - Full ignorance in Bayesian is 1/N to all singletons in Θ
        - mixes lack of belief with disbelief
        - coins : coin head toss = 1/2 iff the coin is fair
        - Bel(\Theta) = 1 is only statement to make, but regardless Bayesian assigns 1/2 to all
      - Simple Support Function
        - weight of evidence : -log (1 - s)
      - support
##### Function hierarchy
simple support function C seperable support functions C support functions C belief functions

- SepF : intersection of focal elements should be focal element
- SupF : union of focal elements should be focal element
- Consonant Sup : Separable Support functions for if for all focal elements they are nested, for any 2 focal elements A,B, either A C B or B C A
- $$ Bel(A \Cap B) = min(Bel(A), Bel(B)) $$ # Necessity
- $$ Pl(A \Cap B) = max(Pl(A), Pl(B)) $$ # Possibility function
- CSF
  - f(∅) = 0
  - f(Θ) = 1
  - $$f(A \Cup B) = min(f(A), f(B)) \forall A,B \subseteq \Theta$$
##### Weight of evidence
For simple support functions
- w = - log(1-s)
- m(S) = s, m(Θ) =1-s, $$w \in [0, \infty)$$

###### Vs Bayesian
- Why not Bayesian?
  - p(Θ | x) is dependent on the prior (and the optimization)
    - choice of prior is non objective
###### Other metrics
- Entropy
  - $$ E = − {m(A) log(Pl(A)) | A ⊆ Θ} $$
  - Shannon E for Bayesian
  - entropy = 0 for consonant belief functions
  - maximum entropy for disjoint focal elements and m is distributed equally of all elements
- Specificity
  - $$ S = \sum \lbrace \frac{m(A)} {\vert A \vert} \vert \emptyset \neq A \subseteq Θ \lbrace $$
  - min for Vacuous, max for Bayesian

#### Related Work


#### Data


#### Evaluation


#### Conclusion
Belief functions are generalizations of Bayesian functions, where Belief functions allow probability numbers assigned to subsets (rather than exhaustive singletons) of the frame of reference. They are not additive and allow for links with fuzzy logic, necessity, possibility theory and avoid priors.
Bel(A) = sum of m(B C= A)
m(A) = Bel(A) - sum m(B), B C A

#### Notes

#### Extra References
