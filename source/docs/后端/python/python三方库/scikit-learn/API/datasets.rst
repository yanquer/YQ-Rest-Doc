================================
datasets
================================

load_wine
================================

.. function:: sklearn.datasets.load_wine(*, return_X_y=False, as_frame=False)[source]

  加载并返回 Wine 数据集 (一个经典的多分类的数据集)

  参考: `<https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html>`_

参数
  return_X_ybool, default=False
    当为 True 时, 返回  (data, target) 而不是整个数据对象.

    target及对应的分类结果

  as_framebool, default=False
    当为 True 时, 数据集是 pandas 的 DataFrame 类型, 会自动选择合适的数据类型, target亦是.

    New in version 0.23.

返回值
  dataBunch
    类字典对象, 具有以下属性

    data{ndarray, dataframe} of shape (178, 13)
      数据矩阵. 若 as_frame 参数为 True, 将会是 pandas DataFrame 类型.
    target: {ndarray, Series} of shape (178,)
      数据分类结果. 若 as_frame 参数为 True, 将会是 pandas Series 类型.
    feature_names: list
      数据集的列名称.
    target_names: list
      目标分类的名称.
    frame: DataFrame of shape (178, 14)
      Only present when as_frame=True. DataFrame with data and target.

      New in version 0.23.
    DESCR: str
      数据集描述

  (data, target)tuple if return_X_y is True
    默认为两个 ndarrays 的元组

    - 第一个 shape 是 (178, 13), 每一行都表示一个样本
    - 第二个 shape 是 (178,), 代表对应分类.

举例::

  >>> from sklearn.datasets import load_wine
  >>> data = load_wine()
  >>> data.target[[10, 80, 140]]
  array([0, 1, 2])
  >>> list(data.target_names)
  ['class_0', 'class_1', 'class_2']

