
### 3.2 Testing

在测试时，已有一个训练好的net和一个输入图片，通过接下来的方法分类。首先，把它的大小改为一个提前定义的小图像尺度，称它为Q。我们说Q不必是等于训练的尺度S（将在第四章展示，用多个Q可以提高表现）。然后，网络应用与重新改变大小的测试图像以这样的方式。也就是说，全连接层第一次被转化成卷积层。由此产生的全连接层用于整个图像。结果是一个类别分数图，有着和类别相同数量的通道数。最后，为了观察一个固定大小的类别得分向量，分类得分图在空间上求平均或者求和。我们也通过水平翻转图像来扩充测试集。原始图像和翻转图像的softmax后验平均用于观察最后的图像得分。
由于全连接层网络用于整个图像，因为不需要在测试时多次采样切割图，另外那个样子也会变得低效，因为它需要网络在每一个切割图上重新计算。在相同的情况下，用一个巨大的切割图集，可以提高精度，因为相比于全连接层它导致一个更详细图片的采样。

### 3.3 实施细节

我们用caffe工具实现我们的网络，但是包含一些修改，这些改变允许我们在多个在独立系统上安装的gpu上训练和验证，也允许我们训练和验证在不切割的图像。多gpu训练并行计算数据，可以分开每个batch的训练数据在多个gpu的分支，并且并行在每个gpu上。在gpu批梯度计算完成，将他们求均值来代表整个batch的梯度。梯度计算在每个gpu上是同步的，因此结果和在一个gpu上训练是一样的。
然而更多负责的加速方法在最近提出，

## 4 分类实验



## 学习心得

3×3的卷积叠加模拟更大的卷积核，减小参数。增加非线性。
lrn没有作用
The batch size was set to 256,
momentum to 0.9 The learning rate was initially set to 0.01

we sampled the weights from a normal distribution
with the zero mean and 10 −2 variance. The biases were initialised with zero

https://blog.csdn.net/whz1861/article/details/78111606

batchnorm 会增加资源的消耗，提升训练速度很明显。

https://blog.csdn.net/mmmmmttttff/article/details/51780694?locationNum=5&fps=1

