=================================
完全关闭Theia应用
=================================

对用使用Electron的后端, 旧版本支持直接调用 ``app.quit`` 退出,
新版本编译的程序不暴露app, 所以无法使用此方法.

.. 找了很久发现Thia有个 ``ApplicationShell``, 可以通过它来退出本身及所有子进程.

.. 代码:\:

..   import { injectable, inject } from 'inversify';
..   import { ApplicationShell } from '@theia/core/lib/browser';

..   @injectable()
..   export class MyService {

..     constructor(@inject(ApplicationShell) private readonly shell: ApplicationShell) {}

..     async closeApp() {
..       await this.shell.close();
..     }

..   }

.. 错了, 这个只能浏览器用, 不支持Electron.

待续...





