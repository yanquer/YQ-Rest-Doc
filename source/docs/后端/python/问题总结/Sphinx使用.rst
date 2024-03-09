=====================
Sphinx简单使用
=====================

创建Sphinx项目
=====================

以在当前文件夹下为例

.. code-block:: sh

	yanque@yanquedembp new_doc_rst % sphinx-quickstart ./
	欢迎使用 Sphinx 5.0.0 快速配置工具。

	请输入接下来各项设置的值（如果方括号中指定了默认值, 直接
	按回车即可使用默认值）。

	已选择根路径：./

	有两种方式来设置 Sphinx 输出的创建目录：
	一是在根路径下创建“_build”目录, 二是在根路径下创建“source”
	和“build”两个独立的目录。
	> 独立的源文件和构建目录（y/n） [n]:

	项目名称将会出现在文档的许多地方。
	> 项目名称: study_doc
	> 作者名称: yanque
	> 项目发行版本 []: 0.0.0

	如果用英语以外的语言编写文档,
	你可以在此按语言代码选择语种。
	Sphinx 会把内置文本翻译成相应语言的版本。

	支持的语言代码列表见：
	http://sphinx-doc.org/config.html#confval-language。
	> 项目语种 [en]: zh_CN

	创建文件 /Users/yanque/project/new_doc_rst/source/conf.py。
	创建文件 /Users/yanque/project/new_doc_rst/source/index.rst。
	创建文件 /Users/yanque/project/new_doc_rst/Makefile。
	创建文件 /Users/yanque/project/new_doc_rst/make.bat。

	完成：已创建初始目录结构。

	你现在可以填写主文档文件 /Users/yanque/project/new_doc_rst/source/index.rst 并创建其他文档源文件了。 用 Makefile 构建文档, 例如：
	make builder
	此处的“builder”是支持的构建器名, 比如 html、latex 或 linkcheck。



.. Note::

	注意不要使用独立的source文件夹, 不然使用toctree会存在相对路径的问题, 暂没找到解决方案.
	粗略看了一下源码, make不知道怎么打断点, 看起来感觉是设计存在问题, 作罢.


配置
=====================

配置文件在 ``config.py`` , 默认的主题比较丑

使用 ``html_theme = 'sphinx_rtd_theme'``

安装 ``pip install sphinx_rtd_theme``

报错

``Could not import extension hoverxref.extension``, 安装::

	pip install sphinx-hoverxref

``Could not import extension notfound.extension``::

	pip install sphinx-notfound-page

