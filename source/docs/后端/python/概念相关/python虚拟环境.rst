=========================
python虚拟环境
=========================


.. post:: 2023-02-20 22:06:49
  :tags: python, 概念相关
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


部分说明可见: :ref:`创建Python虚拟环境`

涉及到一个模块 pyvenv

创建虚拟环境::

  python -m venv <虚拟环境名>

``venv`` 支持的选项

--system-site-packages
  是否使用全局环境的第三方库, 默认否
--without-pip
  不安装pip, 默认会装
--clear
  如果创建虚拟环境的目录已经有了其他虚拟环境，删除重建

会默认在当前环境下创建一个虚拟环境.
是否使用系统的包等信息配置在此目录下的 pyvenv.cfg 文件里,
其中:

- home 表示环境变量, python相关的一些指令就是从这个环境变量指定的目录下找

导入虚拟环境::

  source 虚拟环境名/bin/active
  .


启动
=================

启动

.. code-block:: sh

  # 当前目录下存在名为 venv_test_env 的虚拟环境
  . venv_test_env/bin/activate

关闭
=================

关闭

.. code-block:: sh

  # 当前目录下存在名为 venv_test_env 的虚拟环境
  # deactivate 默认已经写到环境变量里面了, 记得如果有用shell, 使用时不要覆盖此函数
  deactivate

