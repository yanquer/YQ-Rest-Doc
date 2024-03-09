=======================================
命令行工具
=======================================

参考: `<https://docs.scrapy.org/en/latest/topics/commands.html>`_

配置文件位置::

  优先级最低 系统配置 /etc/scrapy.cfg or c:\scrapy\scrapy.cfg
  优先级普通 用户配置 ~/.config/scrapy.cfg ($XDG_CONFIG_HOME) and ~/.scrapy.cfg ($HOME)
  优先级最高 项目配置 scrapy.cfg

实际生效的配置将会合并上述所有的配置,

支持的环境变量配置::

  SCRAPY_SETTINGS_MODULE (see Designating the settings)
  SCRAPY_PROJECT (see Sharing the root directory between projects)
  SCRAPY_PYTHON_SHELL (see Scrapy shell)

配置共享多个项目
=======================================

.. note::

  多个项目都需要在当前目录

scrapy.cfg 下定义多个项目(目录)的 ``scrapy.cfg``::

  [settings]
  default = myproject1.settings
  project1 = myproject1.settings
  project2 = myproject2.settings

默认情况下, scrapy 执行会使用 ``default``, 使用 ``SCRAPY_PROJECT`` 环境变量来
切换不同项目::

  $ scrapy settings --get BOT_NAME
  Project 1 Bot
  $ export SCRAPY_PROJECT=project2
  $ scrapy settings --get BOT_NAME
  Project 2 Bot

使用 scrapy 工具
=======================================

概览::

  Scrapy X.Y - no active project

语法::

  scrapy <command> [options] [args]

支持命令(不需要依赖项目):

startproject
  创建项目

  语法::

    scrapy startproject <project_name> [project_dir]

  project_dir
    项目模块目录名称, 如果不指定, 就跟 myproject 一致

    后续的操作都要cd进目录::

      cd project_dir

其他指令

不依赖项目目录的指令

.. toctree::

  bench
  fetch
  genspider
  runspider
  shell
  settings
  version
  view


依赖项目目录的指令(只有在项目目录下才可以正常执行)

.. toctree::

  check
  crawl
  edit
  list
  parse


.. Custom project commands

自定义项目指令
=======================================

使用 ``COMMANDS_MODULE`` 配置到 scrapy.cfg 实现

.. You can also add your custom project commands by using the COMMANDS_MODULE setting.
.. See the Scrapy commands in scrapy/commands for examples on how to implement your commands.

COMMANDS_MODULE 配置项

默认值: '' (empty string)

.. A module to use for looking up custom Scrapy commands. This is used to add custom commands for your Scrapy project.

Example::

  COMMANDS_MODULE = "mybot.commands"

通过 setup.py 入口注册

.. note::

  也可以通过额外的库注册

.. You can also add Scrapy commands from an external library by adding a scrapy.commands section in the entry points of the library setup.py file.

.. The following example adds my_command command:

比如::

  from setuptools import setup, find_packages

  setup(
      name="scrapy-mymodule",
      entry_points={
          "scrapy.commands": [
              "my_command=my_scrapy_module.commands:MyCommand",
          ],
      },
  )



