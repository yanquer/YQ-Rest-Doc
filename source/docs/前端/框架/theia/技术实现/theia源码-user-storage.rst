============================================
theia源码之user-storage
============================================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, theia, 技术实现
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


.. note::

  此文基于 ``@theia`` 版本 **1.43.1**

此篇幅涉及到的是theia配置相关

比如 theia 默认的配置目录为::

  {家目录}/.theia

默认配置-EnvVariablesServerImpl
============================================

默认的环境配置为 ``EnvVariablesServerImpl``,
源码位置: ``@theia/core/src/node/env-variables/env-variables-server.ts``

源码很简单, 这里只说下它做了什么:

- 实例化时候就配置 ``configDirUri``,
  优先将 ``process.env.THEIA_CONFIG_DIR`` (即环境变量THEIA_CONFIG_DIR) 设置为配置根目录;
  若不存在, 再将 ``join(homedir(), '.theia')`` 设置为配置根;

  或者说设置为 ``configDirUri``
- 其他就是将系统传入的环境变量解析下, 可以通过 ``getVariables()`` 获取
- 等...

user-storage映射
============================================

如果你有跟过theia首选项保存的断点,
很容易就发现, 保存时候使用的 uri 为::

  user-storage:/user/settings.json

这实际上是一个抽象的虚拟映射路径, 映射关系定义在 ``UserStorageContribution``,
位置: ``@theia/userstorage/src/browser/user-storage-contribution.ts``

它通过 默认配置-EnvVariablesServerImpl_ 提供的 ``configDirUri`` 来定义映射关系,
比如::

  user-storage:/user/settings.json

的默认本地磁盘位置为::

  {homedir}/.theia/settings.json

**createProvider** 是具体的实现(只截取关键部分)::

  uriConverter: {
      to: resource => {
          const relativePath = UserStorageUri.relative(resource);
          if (relativePath) {
              return configDirUri.resolve(relativePath).normalizePath();
          }
          return undefined;
      },
      from: resource => {
          const relativePath = configDirUri.relative(resource);
          if (relativePath) {
              return UserStorageUri.resolve(relativePath);
          }
          return undefined;
      }
  }

完


