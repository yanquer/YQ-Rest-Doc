========================================
lbfgs failed to converge
========================================

完整报错信息::

  /Users/yanque/Project/Code/Pycharm/StudyPytorch/.venv/lib/python3.10/site-packages/sklearn/linear_model/_logistic.py:469: ConvergenceWarning: lbfgs failed to converge (status=1):
  STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

  Increase the number of iterations (max_iter) or scale the data as shown in:
      https://scikit-learn.org/stable/modules/preprocessing.html
  Please also refer to the documentation for alternative solver options:
      https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
    n_iter_i = _check_optimize_result(

这是说训练模型的时候，参数的迭代次数达到了限制（默认 max_iter=100），
但是两次迭代参数变化还是比较大，仍然没有在一个很小的阈值以下，这就叫没有收敛。

不过，这只是一个警告（温馨提示）而已，我们可以选择

1. 忽略. 如代码显示忽略: ``import warnings; warnings.filterwarnings("ignore")``
2. 增大最大迭代次数, 如: ``LogisticRegression(max_iter=1000)``
3. 更换其他的模型或者那个参数 solver, 如: ``LogisticRegression(solver="sag")``
4. 将数据进行预处理，提取更有用的特征
