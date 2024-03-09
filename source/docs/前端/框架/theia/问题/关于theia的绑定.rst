================================
关于theia的绑定
================================

自定义拓展可见 :doc:`./创建自定义拓展`

一般来说, 自定义拓展都需要在package.json声明入口文件::

  "theiaExtensions": [
    "hello-world/lib/browser/hello-world-frontend-module"
  ]

入口文件内一般都是相应的绑定::

  import { ContainerModule } from '@theia/core/shared/inversify';

  export default new ContainerModule(
      (bind, unbind, isBound, rebind, unbindAsync, onActivation, onDeactivation) => {
          // add your contribution bindings here
          bind(CommandContribution).to(HelloWorldCommandContribution);
          bind(MenuContribution).to(HelloWorldMenuContribution);
  });

这里介绍一下 bind, unbind, rebind.

rebind
  此前所有相应的绑定皆失效, 但是作用范围保留(如单例)
unbind
  取消此前所有的响应绑定及作用范围
bind
  绑定贡献点, 服务等

  - bind(A).toSelf() 对象即自己, 每次使用都是一个新的对象
  - bind(A).toSelf().inSingleScope() 单例的绑定自己
  - bind(A).toService(B): 注入A时, 实际是类B的对象, 类B的对象需要提前bind





