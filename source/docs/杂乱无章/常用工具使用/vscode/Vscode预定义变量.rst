================================
vscode预定义变量
================================


.. post:: 2024-03-09 18:21:01
  :tags: vscode
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


预定义变量
================================

.. csv-table:: 支持下面的预定义变量:
	:delim: :

	${workspaceFolder}			: 当前工作目录(根目录)
	${workspaceFolderBasename}	: 当前文件的父目录
	${file}						: 当前打开的文件名(完整路径)
	${relativeFile}				: 当前根目录到当前打开文件的相对路径(包括文件名)
	${relativeFileDirname}		: 当前根目录到当前打开文件的相对路径(不包括文件名)
	${fileBasename}				: 当前打开的文件名(包括扩展名)
	${fileBasenameNoExtension}	: 当前打开的文件名(不包括扩展名)
	${fileDirname}				: 当前打开文件的目录
	${fileExtname}				: 当前打开文件的扩展名
	${cwd}						: 启动时task工作的目录
	${lineNumber}				: 当前激活文件所选行
	${selectedText}				: 当前激活文件中所选择的文本
	${execPath}					: vscode执行文件所在的目录
	${defaultBuildTask}			: 默认编译任务(build task)的名字
