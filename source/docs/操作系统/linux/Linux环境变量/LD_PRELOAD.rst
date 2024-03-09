===========================
LD_PRELOAD
===========================

可以用来执行程序运行前首先加载的动态库,
多个使用冒号分割,
与Mac的 :doc:`/docs/操作系统/Mac/Mac环境变量/DYLD_INSERT_LIBRARIES`
基本一致

用例: :doc:`/docs/安全/逆向工程/实战-Ubuntu16下Hook系统的open`

LD_PRELOAD指定的动态库如果与其他的动态库有同名函数,
则会覆盖掉后者的调用

可以使用 dlsym 来自己重调用后续的同名函数::

  dlsym(RTLD_NEXT,"函数名");

.. note::

  dlsym 的头文件是 ``<dlfcn.h>`` ,
  依赖于: ``libdl.so``

  如果没有需要先安装::

    apt install libc6-dev

  编译的时候如果找不到::

    gcc -ldl ...


