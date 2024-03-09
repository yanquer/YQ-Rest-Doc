=====================================
impute
=====================================

.. function:: sklearn.impute.SimpleImputer

  如使用自定义预处理方法处理缺失值::

    from sklearn.impute import SimpleImputer

    imputer = SimpleImputer(strategy='mean')
    X_train_clean = imputer.fit(X_train)




