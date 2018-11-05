# overfeat笔记

 The weights in the network are initialized randomly with (µ,σ) = (0,1 × 10 −2 ). They are then updated by stochastic gradient descent, accompanied by momentum term of 0.6 and an ℓ 2 weight decay of 1 × 10 −5 . The learning rate is initially 5 × 10 −2 and is successively decreased by a factor of 0.5 after (30,50,60,70,80) epochs
 
用卷积层作为特征提取，然后加入不同fcn，来预测不同的问题，把分类，定位、检测三个问题合为一体。

分类其实和alex差不多，就是预测策略有些变化，不实用。
定位的话，通过加入一个层4个单元的来预测box的位置，预测位置也是一种策略，然后和分类的类别对应，找到对应的类别，然后合并。
检测在论文中没有细说，论文中就是加入了一些思想。

https://www.cnblogs.com/liaohuiqiang/p/9348276.html

https://blog.csdn.net/App_12062011/article/details/60956357