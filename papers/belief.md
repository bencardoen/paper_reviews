# Belief theory
### Source
Classic Works of the Dempster--Shafer Theory of Belief Functions, R.Yager, L. Liu, 1st chapter.
## Definitions
* Frame of discernment
$$ \Theta $$
E.g. one asks : who committed a crime, Θ = {John, Robert, David}, problem specific.

* Belief function
$$ Bel : 2^\Theta \rightarrow [0,1] $$

* Probability numbers / mass functions
$$ \sum \lbrace m(A) \vert A ⊆ \Theta \rbrace = 1, m(\emptyset) = 0 $$
A is a focal element, m(A) is not further divided.
$$ Bel(A) = \sum \lbrace m(B) \vert B \subseteq A \rbrace $$
$$ m(A) = Bel(A) - \sum \lbrace m(B) \vert B \subset A \rbrace $$

* Plausibility
$$ Bel(A) \neq Bel(\neg A) $$
It can, but does not have to be
$$ Pl(A) = 1 - Bel(\neg A) $$
$$ Bel(A) \leq Pl(A) $$
$$ Pl(A) = \sum \lbrace m(B) \vert A \cap B \neq ∅ \rbrace $$

$$ B subset A \Rightarrow Bel(A) \geq Bel(B) \land Pl(A) \geq Pl(B) $$

##### Axioms

1. Bel(∅) = 0
2. Bel(\Theta) = 1
3. $$ \forall n \in N, A_1, ... , A_n \subset \Theta, Bel(\cup_{i=1}^n A_i) \geq \sum_{I \subset \lbrace 1, \dots, n  \land I \neq ∅\rbrace} (-1)^{\vert I \vert + 1} Bel(\cap_{i \in I} A_i) $$

##### Encoding of evidence
- Tabular form where several m functions label Θ
- Full Belief function form

##### Combination rule (Dempster)
$$ m(A) = \frac{\sum \lbrace m_1(B) m_2(C) \forall B \cap C = A} {\sum \lbrace m_1(B) m_2(C) \forall B \cap C \neq \emptyset} $$

##### Total weight of conflict
$$ W = \log \frac{1}{\sum \lbrace m_1(B) m_2(C) \forall B \cap C \neq \emptyset} $$

##### Hierarchy of belief functions
$$ V \subset SiF \subset SeF \subset SuF \subset Be $$

* Vacuous : full ignorance, \Theta is not divded.
  * Contrast with Bayesian where uniformity is used instead of ignorance (m(A) = 1/n, |A| = 1)
* Simple support (SiF) : 2 focal elements, S and Θ, m(S) = s and m(Θ) = 1-s
  * weight of evidence w = -log(1-s)
* Bayesian : |A| = 1 for all A ⊂ Θ
  * Bel(A ∪ B) = Bel(A) + Bel(B) if A ∩ B = ∅
* Separable (Sef)
  * A,B focal elements, and A \cap B ⪇ ∅ ⇒ A ∩ B = focal
  * Consonant support functions (CoSef)
    * All focal elements are nested, forall A, B: A ⊂ B or B ⊂ A
    * Directional precision
    * $$ Bel(A \cup B) = min(Bel(A), Bel(B)) $$
    * $$ Pl(A \cup B) = max(Bel(A), Bel(B)) $$
    * Cosef Bel = necessity function in possibility theory
    * Cosef Pl = possibility
* Support function : Bel and union of all focal elements is also a focal element

###### Entropy and specifity
Entropy is measure of disorder (Shannon for Bayesian), E = 0 for consonant belief, maximal for uniform disjoint focal with equal probability.
* $$ E = - \sum \lbrace m(A) log(Pl(A)) \vert A \subseteq Θ \rbrace $$

Specifity is the measure indicating by how much a single focal element explains the event.
* $$ S = - \sum \lbrace \frac{m(A)}{\vert A \vert} \vert \emptyset \neq A \subseteq Θ \rbrace $$




##### Concepts
- Belief functions are not (necessarily) additive
  - Example: Ignorance, truth is in Θ but no information (prob or log) justifies allocation of truth. Hence Bel(Θ) = 1, Bel(A) = 0 for all propers subsets of Θ
- Bayesian functions are belief functions where each focal element is a singleton
- Belief is a measure of evidential support
- $$B \subset A \Rightarrow B > A $$
  - iow B is a stronger (more specific) proposition than A requiring stronger evidence
  - evidence for A does not translate (always) to B
  - m(A) > m(B) does not need to hold
- mass functions are good to encode evidence, plausibility/belief expresses intuitive impact of the evidence

#### Notes

- Heidelberg: An observation cannot predict a result with certainty, the probability of a certain result can be checked by repetition
- Pure evidence : proves a certainty with a numerical probability without assigning the remainder to the negation
- Mixed evidence : proves a certainty with a numerical probability and assigns the remainder to the negation
