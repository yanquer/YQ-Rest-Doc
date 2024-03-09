============================
cmakelists.txt编写
============================

cmakelists.txt是基于cmake指令的.

普通变量
============================

使用 ``set(var value)`` 赋值, 使用 ``${}`` 方式取值,但是在IF控制语句中是直接使用变量名


获取环境变量
============================

使用 ``$ENV{}`` 方式取值,使用 ``SET(ENV{VAR} VALUE)`` 赋值


定义bool变量
============================

使用 set, 以下相当 bool DEBUG = True ::

	SET(DEBUG ON)

OFF 就是 False

.. note::

	像set这种关键字不区分大小写, 但是变量名区分大小写;

	使用 if 语句时, 直接使用变量名, 不需要用花括号包裹

打印输出
============================

使用 MESSAGE ::

	MESSAGE("DEBUG=" ${DEBUG})

执行cmake指令
============================

使用execute_process


创建文件夹
----------------------------

使用 execute_process, 创建一个newdir, 注意定义 new_dir::

	execute_process( COMMAND ${CMAKE_COMMAND} -E make_directory ${new_dir})

复制文件夹
----------------------------

使用 execute_process, 将dir1复制到dir2, 注意定义 dir1 dir2::

	execute_process( COMMAND ${CMAKE_COMMAND} -E copy_directory ${dir1} ${dir2})

复制文件
----------------------------

使用 execute_process, 将file1复制到file2, 注意定义 file1 file2::

	execute_process( COMMAND ${CMAKE_COMMAND} -E copy ${file1} ${file2})

添加子目录的CMakeLists.txt
============================

如, 在根目录下, 新建Stack目录, 在Stack中建立一个CMakeLists.txt文件

根目录需增加如下语句::

	add_subdirectory(Stack)

更多见: :doc:`/docs/后端/c/cmake`
