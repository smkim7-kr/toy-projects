# ArcFace-visualization

This is an reimplementation of toy examples in the paper [ArcFace: Additive Angular Margin Loss for Deep Face Recognition](https://arxiv.org/abs/1801.07698). 



<video src="2d_arcface_toy.mp4"></video>

### Details

* Dataset: FashionMNIST
* Model: Custom three convolutional layers with Max-pooling layers
* Epochs: 30
* Others: Increased linear margin(m) linearly from 0 to 0.5 to overcome problems associated with bottleneck 2d/3d for plotting

Further implementation details can be found on Colab notebooks on [FashionMNIST-2d](https://colab.research.google.com/drive/1FnNCo5brwxPXxoRpYV1brtH_PMMWV64M#scrollTo=Suxp-vWSPML1&uniqifier=2) and [FashionMNIST-3d](https://colab.research.google.com/drive/1ia9fk-6SDxNcvRW67Rsg0XBfQ4f2MTRg#scrollTo=LqsPWZaSBiK7).



### Results

* 2d

  * epoch 1![epoch0](epochs/epoch0.png?raw=true)
  * epoch 10![epoch10](epochs/epoch10.png?raw=true)

  * epoch 20![epoch21](epochs/epoch21.png?raw=true)

  * epoch 30![epoch28](epochs/epoch28.png?raw=true)

* 3d
  * Left: Softmax / Right: ArcFace![3d](3d.JPG?raw=true)

### References

* https://github.com/sweetcocoa/toy/tree/master/arcface by sweetcocoa

