=====================
mac一直弹登录项
=====================


清空登录项::

  sfltool resetbtm

或者改权限: 555


- sfltool dumpbtm: 打印登录项和后台项的当前状态，包括载入的 servicemanagement 有效负载 UUID。
- sfltool resetbtm：还原登录项和后台项数据。如果在测试间使用此命令，建议用户也重新启动自己的电脑。

见: `在 Mac 上管理登录项和后台任务 <https://support.apple.com/zh-cn/guide/deployment/depdca572563/web>`_
