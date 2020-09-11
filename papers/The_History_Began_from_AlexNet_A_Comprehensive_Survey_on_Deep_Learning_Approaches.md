## Title
The History Began from AlexNet: A Comprehensive Survey on Deep Learning Approaches
### MetaData
##### Url
10.1016/S0011-9164(00)80105-8
##### Type
review

##### Domain
CS

##### Keywords
deep learning, machine learning, optimization, inverse problems


##### Cite

```LaTex

```
## Content
#### Research Question
Review of DL

#### Contribution


#### Method
##### Problem types
* supervised: y = f(x), given x, predict y. During training, have (x,y) pairs
* semi-supervised: y = f(x), given x, predict y. During training have subset of (x,y) pairs
* unsupervised: y=f(x), given x, predict y. No labelled pairs available
* reinforcement: optmized function is not available, except through interaction, and is state based, y=f(x, a). subset of (x,y) pairs are available, a is unknown (modelled state)
  * few parameters, RL
  * high pspace, DRL
##### Machine Learning
###### Handcrafted feature (s extraction)
* Histogram Oriented Gradient
* Local Binary Pattern
* ...
###### Learners
* SVM
* RanFor
* PCA
* KPCA
* Linear Decrement Analysis (LDA)
* Fisher Decrement Analysis (FDA)
* Boosting (use k algorithms)


###### DL vs ML
* ML vs DL : output of ML is feature to class mapping, DL output is features + feature mapping

###### When to apply DL
* no human expert
* unable to explain human expertise
* time axis
* size is too vast
* specific case

###### Challenges
* Causality in data
* Energy efficient
* Transfer learning
* Interpretability

###### DNN concepts
* Neuron: accepts sum of weighted inputs, applies (activation) function, output
* Chain neurons: ANN
* (Stochastic) Gradient Descent to optimize model (weights) in function of loss (error)
* Momentum: add momentum of gradient instead of gradient to prevent local optimum, momentum set to 0.5, then increased to .9 later stages. Higher value overshoots, can be unstable, only used in later stages
  * SGD: for batch(x,y) in ran(X,Y):
  * y' = f_o(x)
  * o = o - n * 1/n sum d (e(y', y)) / do
* Learning rate: constant, factored, exp decay. Learning rate too large can diverge, too small will take ages: n_t = n_0 b^{t/e}   b in (0,1). B set to 0.1 to decay learning rate by factor 10
* Regularization: Add size of weights to loss function, L(F, x, y) = e(f(x), y) + l |o|^2

###### Convolutional Neural Network
* CNN max pooling insensitive to variation
* sparse connections = faster
* Alternates convolational layer with max pooling layer
* Convolutional layer applies kernel, convolutional filter with a certain size slides over input to generate single scalar output
* Classification layer with fc feed forward, leads to exponential weights
* Subsampling layer (pooling)
* Stride size increases receptive field, decreases output volume
* Padding adds (zero) padding to keep spatial size
* ReLu : f(x) = max(0, x), faster than sigmoid without affecting cost
* Max pooling: prevents overfitting (max instead of avg)
* Batch Normalization: output activation - mean batch * sd batch
* Optimizers:
    * EVE

###### SoA
* AlexNet
    * Local Response Normalization (LRN)
    * Dropout
* VGGNet
    * Depth matters
* GoogleNet
    * Add variable filters (1/5/3)
* ResNet
    * Solve V gradient by
        * In -|-> Conv -> Conv > + output
        *     | ---- bpass       |
* Inception / ResNet
    * In --> 1 / 3 /   | 1 conv
    * In --> 1 / 3 / 5 |  conv
    * In -->                     | + out
* DenseNet
    * Connect conv block i with i+1, i+2, ...
* CapsuleNet
    * Tackles inability of CNN for

###### RNN
* Sequential input
* LSTM
* GRU

###### Autoencoder
* Input --> Feature Map --> output
* Loss = e(In, Out)
* Deep AE have vanishing gradient
* Variational Auto Encoder
    * latent vector is mean, std
* Restricted Boltzmann machines

###### GAN
* Generator uses latent (noise) vector with Gaussian to generate samples
* Discriminator is asked to differentiate between generated samples and truth
* Both D, G in zero sum game
* Wasserstein GAN

###### DRL
* Q learning
    * Q(state, action) = reward(state, action) + j max_a'(Q(s', a'))
* Q learning (probabilistic) will converge iff all states are sampled infinitely
* DRL : Replace Q by DNN taking in state/environment

###### Transfer Learning
* pre trained weights for different tasks
* New data : Small / large
* Dataset : Similar/Different
* Large data: fine tune
* Small data: freeze weights, train linear classifier on top/all level

###### Faster/Leaner
* Binary Connected Neural Networks: convert fp mult to binary addition (\*7 on GPU)
* 

#### Related Work


#### Data


#### Evaluation


#### Conclusion


#### Notes
https://adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks-Part-2/
#### Extra References
