# alexnet学习笔记

模型深度与卷积层数很重要

batchNormaliztion 有助于训练，会加速训练

sgd   SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
很不错的一个参数， , momentum of 0.9, and weight decay of 0.0005

高级的优化方法，不一定好，sgd很快。

模型的参数大小主要在 flat后的全连接层。

lrn （local respond normal）在次论文中说会提高精度，但是在vgg中推翻了这个想法

数据增强。

relu可以避开饱和区，加速训练

maxpooling 步长小于size，可以提高采样精度。

dropout可以防止过拟合，在训练中，影响了训练时间。

这个论文中，提出了随机切割的想法，256的图片，随机选出224的大小图片几个，