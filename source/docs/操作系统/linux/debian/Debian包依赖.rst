===============================
Debian包依赖
===============================


.. post:: 2024-02-21 21:55:17
  :tags: linux, debian
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


要知道package的依赖方案

可以直接看报错地方的源码的要求
也可以直接::

  apt-cache show $package

有些涉及到了系统的包没法操作的话::

  apt-get install aptitude
  aptitude insatll $package		#这里会给出依赖方案，选一个可行的

  apt-get insatll $package


