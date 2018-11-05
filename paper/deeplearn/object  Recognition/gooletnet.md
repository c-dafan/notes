# Going deeper with convolutions阅读笔记

论文一开始主要讲了一些现状，和一些精度更高的方法，已经传统的方法

增加模型的深度和宽度是一个有效的方法，但是会有一些问题，比如过拟合。
对付过拟合可以增加数据，但是增加数据的成本很高，所以不合适。
深度增加还有一个问题就是资源不够，而且无法在实践生活中应用。

所以作者有一个想法，通过稀疏链接。（The fundamental way of solving both issues would be by ultimately moving from fully connected
to sparsely connected architectures, even inside the convolutions）

但是计算机对于这种数据are very inefficient when it comes to numerical
calculation on non-uniform sparse data structures。
然后就有一种想法，就像文章中的Inception这种结构来解决这个问题。这种结构比较复杂，所以在第一层卷积用了7x7的卷积核和2的步伐，和3x3（s=2）的maxpooling，减少模型的计算量。

在结构中，用1x1的卷积做非线性变化，作用大致有两个，第一增加非线性，第二节约资源。

训练模型的方法，在论文中也不是很确定，论文中提高用到了很多方法，但是作者也不知道到底是那种方法再起作用。

https://blog.csdn.net/wspba/article/details/61921619