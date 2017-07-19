# ExtraTreesClassifier

极端随机树

第一次看见这个算法，还是在sklearn的[官方api文档中][1],后来发现还挺好用，但是找不到算法的详细内容。通过查看sklearn的源代码发现它和随机深林继承同一个
父类，但是随机森林的单模型是[决策树][3],而这个模型是[ExtraTreeClassifier][2]。另外，ExtraTreeClassifier的父类是决策树，它和决策树有什么不同呢



[1]: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html
[2]: http://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier
