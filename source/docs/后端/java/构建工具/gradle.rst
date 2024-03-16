========================
Gradle
========================


.. post:: 2024-03-09 18:21:01
  :tags: java, 构建工具
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://gradle.org

.. important::

  目前为止, 此文档编写时, 使用版本为 Gradle-8.1.1

安装
========================

Mac可以直接使用homebrew::

  brew install gradle

安装会下载很多依赖包, 不懂Mac为啥要下载这么多依赖包, 我的安装路径是在::

  /usr/local/Cellar/gradle/8.1.1

.. sidebar::

  可能会有需要安装Java, 可参考 :doc:`/docs/后端/java/安装`

然后在Android Studio里面自定义Gradle路径的时候不知道为啥就直接是::

  /usr/local/Cellar/gradle/8.1.1/libexec

.. figure:: /resources/images/ide_gradle_set.jpg
  :width: 480px

  Android Studio中设置位置

所有版本: https://gradle.org/releases/

若需要设置Gradle仓库的环境变量, 设置::

  export GRADLE_USER_HOME=...

.. note::

  若下载的是解压包, 需要手动解压到相关位置, 如::

    $ mkdir /opt/gradle
    $ unzip -d /opt/gradle gradle-8.1.1-bin.zip
    $ ls /opt/gradle/gradle-8.1.1
    LICENSE  NOTICE  bin  getting-started.html  init.d  lib  media

.. warning::

  若使用Mac brew安装, 需要提前配置好JAVA环境, 可参考 :doc:`/docs/后端/java/安装` ,
  若是后配置好JAVA, 需要先brew卸载后再装.
  (最主要的就是跟系统的 `/usr/bin/java` 对应起来, 否则即使配置的正确的JAVA_HOME, 也会有问题)

  所以我选择解压包方便.

配置系统环境
========================

Linux/Mac, 以安装到 `/opt/gradle/gradle-8.1.1` 为例::

  # GRADLE_HOME 官网安装文档并未要求设置
  GRADLE_HOME=/opt/gradle/gradle-8.1.1
  export PATH=$PATH:$GRADLE_HOME/bin

Windows直接在PATH环境变量新增一个即可.

配置镜像源
========================

有两种选择

.. sidebar::

  `.gradle` 目录通常被设置为环境变量 GRADLE_USER_HOME

- 全局配置, 用户目录下新建 `.gradle` 目录,
- 项目配置, 在项目下的 settings.gradle
  增加源地址::

    pluginManagement {
        repositories {

            maven { url 'https://maven.aliyun.com/repository/public/' }
            maven { url 'https://maven.aliyun.com/repository/google/' }
            maven { url 'https://maven.aliyun.com/repository/jcenter/' }
            maven { url 'https://maven.aliyun.com/repository/central/' }

            google()
            mavenCentral()
            gradlePluginPortal()
        }
    }
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {

            maven { url 'https://maven.aliyun.com/repository/public/' }
            maven { url 'https://maven.aliyun.com/repository/google/' }
            maven { url 'https://maven.aliyun.com/repository/jcenter/' }
            maven { url 'https://maven.aliyun.com/repository/central/' }

            google()
            mavenCentral()
        }
    }
    rootProject.name = "hello"
    include ':app'

详细说明/介绍
========================

.. toctree::
  :maxdepth: 1

  gradle/index



