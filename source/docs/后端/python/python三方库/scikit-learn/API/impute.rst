=====================================
impute
=====================================


.. post:: 2023-03-03 23:21:31
  :tags: python, python三方库, scikit-learn, API
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. function:: sklearn.impute.SimpleImputer

  如使用自定义预处理方法处理缺失值::

    from sklearn.impute import SimpleImputer

    imputer = SimpleImputer(strategy='mean')
    X_train_clean = imputer.fit(X_train)




