## Title
Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks
### MetaData
##### Url
http://arxiv.org/abs/1703.03400
##### Type
novel method
##### Domain
CS

##### Keywords
Deep Learning, Meta Learning

##### Cite

```LaTex

```
## Content
#### Research Question
We aim to train models that can achieve rapid adaptation, a problem setting that is often formalized as few-shot learn-ing. In this section, we will define the problem setup and present the general form of our algorithm.

#### Contribution
features that are broadly applicable to all tasks in p(T), rather than a single individual task. How can we en-courage the emergence of such general-purpose representa-tions?

#### Method
Learns model in such a way that they can be quickly fine tuned using SGD.

* T = dist(tasks)
* om = model
* while true
    * Ti subseteq T
    * for t in Ti
        * SGD(om) LossTi (fo) [K examples]
        * om_i' = om - a (SGD(om) LTi(fo)))
    * om = om - b sgd(om) sum t Lt (foi)

#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes

#### Extra References
