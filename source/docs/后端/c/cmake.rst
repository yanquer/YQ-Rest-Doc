=========================
cmake
=========================


.. post:: 2023-02-20 22:06:49
  :tags: c
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


安装
=========================

下载地址: https://cmake.org/download/

执行以下命令设置环境变量::

	sudo "/Applications/CMake.app/Contents/bin/cmake-gui" --install

例如这样的输出::

	yanque@yanquedembp PlantsVsZombies % sudo "/Applications/CMake.app/Contents/bin/cmake-gui" --install
	Password:
	Linked: '/usr/local/bin/cmake' -> '/Applications/CMake.app/Contents/bin/cmake'
	Linked: '/usr/local/bin/ctest' -> '/Applications/CMake.app/Contents/bin/ctest'
	Linked: '/usr/local/bin/cpack' -> '/Applications/CMake.app/Contents/bin/cpack'
	Linked: '/usr/local/bin/cmake-gui' -> '/Applications/CMake.app/Contents/bin/cmake-gui'
	Linked: '/usr/local/bin/ccmake' -> '/Applications/CMake.app/Contents/bin/ccmake'
	yanque@yanquedembp PlantsVsZombies %


基本语法
=========================

- 注释: 使用#
- 命令不区分大小写, 变量区分大小写
- 定义变量: set
  - 定义字符串: set(var1 str_data)
  - 定义列表: set(var_list var1 var2 var3 ...)
  - bool: True就是ON, False就是OFF, 如set(bool_var OFF)
  - 使用美元符加花括号 ``${}`` 来访问定义的变量, 若使用与if语句, 则不需要, 直接使用变量名称即可
  - 访问环境变量: 与普通变量相比, 需要加上 ENV, 如$ENV{VariableName}
- 打印输出: 使用 message, 如message(“var=${var}”)

.. function:: project(<projectname> [languageName1 languageName2 ...])

	指定项目名称, 如指定项目为Game::

		project(Game)

.. function:: cmake_minimum_requried(VERSION major[.minor[.patch)

	用于指定需要的CMake的最低版本, 如指定最低使用2.8版本::

		cmake_minimum_requried(VERSION 2.8)

.. function:: aux_source_directory(<dir> <variable>)

	用于将dir目录下的所有源文件的名字保存在变量variable中, 如::

		aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src  DIR_SRCS)

.. function:: add_executable(<name> [WIN32] [MACOSX_BUNDLE][EXCLUDE_FROM_ALL] source1 source2 … sourceN)

	用于指定从一组源文件source1 source2 ... sourceN 编译出一个可执行文件且命名为name

	使用范例::

		add_executable(Main $(DIR_SRCS))

.. function:: add_library([STATIC | SHARED | MODULE] [EXCLUDE_FROM_ALL] source1source2 … sourceN)

	用于指定从一组源文件 source1 source2 ... sourceN编译出一个库文件且命名为name

	使用范例::

		add_library(Lib $(DIR_SRCS))

.. function:: add_dependencies(target-name depend-target1 depend-target2 …)

	用于指定某个目标（可执行文件或者库文件）依赖于其他的目标。这里的目标必须是add_executable、add_library、add_custom_target命令创建的目标

.. function:: add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])

	用于添加一个需要进行构建的子目录

	使用范例::

		add_subdirectory(Lib)

.. function:: target_link_libraries(<target> [item1 [item2 […]]][[debug|optimized|general] ] …)

	用于指定target需要链接item1 item2 ...。这里target必须已经被创建，链接的item可以是已经存在的target（依赖关系会自动添加）

	使用范例::

		target_link_libraries(Main Lib)

.. function:: set(<variable> <value> [[CACHE <type><docstring> [FORCE]] | PARENT_SCOPE])
	:noindex:

	用于设定变量 variable 的值为 value。如果指定了 CACHE 变量将被放入 Cache（缓存）中。

	使用范例::

		set(ProjectName Main)

.. function:: unset(<variable> [CACHE])

	用于移除变量 variable。如果指定了 CACHE 变量将被从 Cache 中移除。

	使用范例::

		unset(VAR CACHE)

.. function:: message([STATUS|WARNING|AUTHOR_WARNING|FATAL_ERROR|SEND_ERROR] “message todisplay”…)

	用于输出信息

	使用范例::

		message(“Hello World”)

.. function:: include_directories([AFTER|BEFORE] [SYSTEM] dir1 dir2 …)

	用于设定目录，这些设定的目录将被编译器用来查找 include 文件

	使用范例::

		include_directories(${PROJECT_SOURCE_DIR}/lib)

.. function:: find_path(<VAR> name1 [path1 path2 …])

	用于查找包含文件name1的路径，如果找到则将路径保存在VAR中（此路径为一个绝对路径），如果没有找到则结果为<VAR>-NOTFOUND.默认情况下，VAR会被保存在Cache中，这时候我们需要清除VAR才可以进行下一次查询（使用unset命令）::

		find_path(LUA_INCLUDE_PATH lua.h ${LUA_INCLUDE_FIND_PATH})
		if(NOT LUA_INCLUDE_PATH)
			message(SEND_ERROR "Header file lua.h not found")
		endif()

.. function:: find_library(<VAR> name1 [path1 path2 …])

	用于查找库文件 name1 的路径，如果找到则将路径保存在 VAR 中（此路径为一个绝对路径），如果没有找到则结果为 <VAR>-NOTFOUND。一个类似的命令 link_directories 已经不太建议使用了

.. function:: add_definitions(-DFOO -DBAR …)

	用于添加编译器命令行标志（选项），通常的情况下我们使用其来添加预处理器定义

	使用范例::

		add_definitions(-D_UNICODE -DUNICODE)

.. function:: file

	命令简述：此命令提供了丰富的文件和目录的相关操作（这里仅说一下比较常用的）
	使用范例::

		# 目录的遍历
		# GLOB 用于产生一个文件（目录）路径列表并保存在variable 中
		# 文件路径列表中的每个文件的文件名都能匹配globbing expressions（非正则表达式，但是类似）
		# 如果指定了 RELATIVE 路径，那么返回的文件路径列表中的路径为相对于 RELATIVE 的路径
		file(GLOB variable [RELATIVE path][globbing expressions]...)

		# 获取当前目录下的所有的文件（目录）的路径并保存到 ALL_FILE_PATH 变量中
		file(GLOB ALL_FILE_PATH ./*)
		# 获取当前目录下的 .h 文件的文件名并保存到ALL_H_FILE 变量中
		# 这里的变量CMAKE_CURRENT_LIST_DIR 表示正在处理的 CMakeLists.txt 文件的所在的目录的绝对路径（2.8.3 以及以后版本才支持）
		file(GLOB ALL_H_FILE RELATIVE${CMAKE_CURRENT_LIST_DIR} ${CMAKE_CURRENT_LIST_DIR}/*.h)

常用变量
=========================

常用变量::

	UNIX 	如果为真，表示为UNIX-like的系统，包括AppleOSX和CygWin
	WIN32 	如果为真，表示为 Windows 系统，包括 CygWin
	APPLE 	如果为真，表示为 Apple 系统
	CMAKE_SIZEOF_VOID_P 			表示void*的大小（例如为4或者8），可以使用其来判断当前构建为32位还是64位
	CMAKE_CURRENT_LIST_DIR 			表示正在处理的CMakeLists.txt文件的所在的目录的绝对路径(2.8.3以及以后版本才支持)
	CMAKE_ARCHIVE_OUTPUT_DIRECTORY 	用于设置ARCHIVE目标的输出路径
	CMAKE_LIBRARY_OUTPUT_DIRECTORY 	用于设置LIBRARY目标的输出路径
	CMAKE_RUNTIME_OUTPUT_DIRECTORY 	用于设置RUNTIME目标的输出路径



:参考::
	https://blog.csdn.net/qq_23123181/article/details/122736393?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-122736393-blog-80902807.pc_relevant_recovery_v2&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-122736393-blog-80902807.pc_relevant_recovery_v2&utm_relevant_index=3
	https://blog.csdn.net/zhanghm1995/article/details/80902807


