===================================
jupyter
===================================


.. post:: 2023-03-03 23:21:31
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


jupyter notebook 是一个网页形式的编辑器,
支持 在网页页面中直接编写代码和运行代码，
代码的运行结果也会直接在代码块下显示的程序。
如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

安装::

  pip install jupyter

启动::

  jupyter notebook

结果就是在 当前目录 启动一个 jupyter 服务器,
一般就会自动跳到浏览器打开, 或者手动打开也行::

  http://localhost:8888/tree

.. note::

  jupyter生成的文件不是纯正的 py 文件

MacOS下快捷键::

  Enter               在当前单元格换行
  Command + Enter     执行当前单元格
  Ctrl + Enter        执行当前单元格
  Shift + Enter       执行当前单元格并新建一个单元格


jupyter notebook支持的选项
===================================

-h, --help    帮助信息
--port <port_number>
  指定启动端口
--no-browser  启动但是不自动打开浏览器
--generate-config
  生成默认配置文件

