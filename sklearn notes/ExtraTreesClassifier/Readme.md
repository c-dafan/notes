# ExtraTreesClassifier

极端随机树

第一次看见这个算法，还是在sklearn的[官方api文档中][1],后来发现还挺好用，但是找不到算法的详细内容。通过查看sklearn的源代码发现它和随机深林继承同一个
父类，但是随机森林的单模型是[决策树][3],而这个模型是[ExtraTreeClassifier][2]。另外，ExtraTreeClassifier的父类是决策树，它和决策树有什么不同呢？

![sklearn 截图](https://github.com/c-dafan/notes/blob/master/sklearn%20notes/ExtraTreesClassifier/1.png)

有意思它不能单独使用，与决策树不同在于 DecisionTreeClassifier在划分结点的时候，选取的是最优的特征划分的，而这个ExtraTreeClassifier是随机选取 max_features个特征，然后从这个里面选取最优的进行划分。

ExtraTreesClassifier与随机森林源代码不同在

![代码截图](https://github.com/c-dafan/notes/blob/master/sklearn%20notes/ExtraTreesClassifier/2.png)

![代码截图](https://github.com/c-dafan/notes/blob/master/sklearn%20notes/ExtraTreesClassifier/3.png)

ExtraTreesClassifier模型bootstrap参数默认是False，随机森林是True 。若为true，则是Bootstrap Sample (有放回抽样)。



[1]: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html
[2]: http://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier
[3]: http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
