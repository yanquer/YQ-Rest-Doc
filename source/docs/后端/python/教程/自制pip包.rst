=============================
自制pip包
=============================

自制pip包, 打包为 whl / tar.gz 格式

首先需要自己的一份源码, 一般结构如下,
src目录下是自己的源代码, 注意要有 `__init__` 文件表示是一个python模块::

  ├── LICENSE
  ├── README.md
  ├── pyproject.toml
  ├── setup.py
  └── src
      ├── __init__.py
      └── win_clip_file.py

其他根目录下文件是相关配置, 其中setup.py是生成脚本,

一般内容如下, 根据实际修改::

  from setuptools import setup, find_packages

  setup(name='win_clipboard',
        version='0.0.1',
        description='to windows, copy file',
        # long_description='',
        # long_description_content_type="text/markdown",  # 模块详细介绍格式
        # url="github地址",  # 模块github地址
        author='yan que',
        author_email='yanquer@qq.com',
        requires=['win32clipboard', ],  # 定义依赖哪些模块
        # packages=find_packages(),  # 系统自动从当前目录开始找包
        # 如果有的文件不用打包，则只能指定需要打包的文件
        packages=['win_clipboard', ],  # 指定目录中需要打包的py文件，注意不要.py后缀
        # 模块相关的元数据（更多的描述）
        #     classifiers=[
        #         "Programming Language :: Python :: 3",
        #         "License :: OSI Approved :: MIT License",
        #         "Operating System :: Independent",
        #     ],
        # 依赖模块
        install_requires=[
            "pywin32"
        ],
        # python版本
        python_requires=">=3",
        license="apache 3.0"
        )

setup参数说明:

name
  打包后包的文件名
version
  版本号
author
  作者
author_email
  作者的邮箱
py_modules
  要打包的.py文件
packages
  打包的python文件夹
include_package_data
  项目里会有一些非py文件,比如html和js等,这时候就要靠include_package_data 和 package_data 来指定了。

  package_data:一般写成{‘your_package_name’: [“files”]}, include_package_data还没完,还需要修改MANIFEST.in文件.

  MANIFEST.in文件的语法为: include xxx/xxx/xxx/.ini/(所有以.ini结尾的文件,也可以直接指定文件名)
license
  支持的开源协议
description
  对项目简短的一个形容
ext_modules
  是一个包含Extension实例的列表,Extension的定义也有一些参数。
ext_package
  定义extension的相对路径
requires
  定义依赖哪些模块
provides
  定义可以为哪些模块提供依赖
data_files
  指定其他的一些文件(如配置文件),规定了哪些文件被安装到哪些目录中。
  如果目录名是相对路径,则是相对于sys.prefix或sys.exec_prefix的路径。如果没有提供模板,会被添加到MANIFEST文件中

打包::

  python setup.py bdist_wheel # 打包为whl文件
  python setup.py sdist # 打包为tar.gz文件

会生成在当前目录下dist文件夹下面

若需要上传到pypi
需要先去注册账号 https://pypi.org/

上传需要安装twine::

  pip install twine
  twine upload dist/*
  # 输入刚注册的用户名密码就能上传。







