## Title
A Sub-Quadratic Exact Medoid Algorithm
### MetaData
##### Url
http://proceedings.mlr.press/v54/newling17a/newling17a.pdf
##### Type
method

##### Domain
Biology

##### Keywords
smlm, double labelling analysis



##### Cite
e.g. BibLatex
```LaTex
your cite code here

```
## Content
#### Research Question
We present a new algorithm trimed for ob- taining the medoid of a set, that is the el- ement of the set which minimises the mean distance to all other elements.
#### Contribution


#### Method
- E(i) = 1/(N-1) \sum_{j \in N \setminus i} d(x(i), x(j))
- assumption of 1 medoid
- mean/median may not exist or make sense
- related is geometric median
  - $$ g(S) = \argmin{v\inV} (\sum_{y \in S} ||v-y||) (vector space R^d)
  - fast, but in practice not always applicable (need vector space, not network space)
##### Algorithm
Input : x(1..N)
Output : medoid
```
l = zeros(N,1)
mcl = -1
Ecl = infty
for i in shuffle(1..N) do
  if l[i] < Ecl
    for j in 1..N
      d[j] = dist(x(i),x(j))
    l[i] = 1/(N-1) sum_j d(j)
    if l[i] < Ecl
      mcl, Ecl = i, l[i]
    for j in 1..N
      l[j] max( l(j), |l(i)-d(j))
m*, E* = mcl, Ecl
return x[m*]
```

#### Related Work
 - outperforms approximation algorithms

#### Data
- synthethic benchmark data sets

#### Evaluation
- eveluations/accuracy

#### Conclusion
Fast accurate mediod algorithm

#### Notes

#### Extra References
