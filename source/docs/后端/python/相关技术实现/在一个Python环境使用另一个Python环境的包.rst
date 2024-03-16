=============================================
在一个Python环境使用另一个Python环境的包
=============================================


.. post:: 2023-02-20 22:06:49
  :tags: python, 相关技术实现
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


仅针对三方包.

需求:
  当使用一个虚拟环境时, 想导入另一个虚拟环境的三方包

主要有两种解决方案

- 手动安装需要的包_ : 使用 pip freeze 导出另一个虚拟环境的三方包信息到 requirements.txt, 然后手动安装
- 配置环境变量PYTHONPATH_ : 将另一个虚拟环境的三方包加入到环境变量 PYTHONPATH

手动安装需要的包
=============================================

大致::

  source /path/to/venv_b/bin/activate
  pip freeze > /path/to/requirements.txt
  source /path/to/venv_a/bin/activate
  pip install -r /path/to/requirements.txt


.. note::

  不确定直接::

    sys.path.insert(...)

  是否可行, 有时间实验一下

配置环境变量PYTHONPATH
=============================================

找到另一个虚拟环境的三方包目录::

  source /path/to/venv_b/bin/activate
  python -c "import site; print(site.getsitepackages())"

将虚拟环境b的 site-packages 目录添加到 PYTHONPATH 环境变量中(也可以直接在Python的os.environ中设置)::

  export PYTHONPATH=$PYTHONPATH:/path/to/venv_b/lib/pythonX.Y/site-packages

在虚拟环境a中调用虚拟环境b的包::

  source /path/to/venv_a/bin/activate
  python
  import module_name
