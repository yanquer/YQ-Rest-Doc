======================
pytest-rerunfailures
======================

支持使用 :doc:`/docs/后端/python/教程/Pytest` 时候的重试.

安装::

    pip3 install pytest-rerunfailures

使用::

    # --reruns 5        重试五次
    # --reruns-delay 2  每次重试间隔2秒
    pytest --reruns 5 --reruns-delay 2 -s

选项参数
======================

--reruns=<int>      执行失败时重试次数
--reruns-delay=<int>
                    执行失败重试之间的间隔



