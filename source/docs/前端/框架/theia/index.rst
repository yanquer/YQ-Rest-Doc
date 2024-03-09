======================
Theia
======================

一个IDE框架, 前后端分离的架构

以插件的形式编写代码, 支持依赖注入

后端可选浏览器/Electron

注意使用 rawProcessFactory 创建的进程可能受
ProcessManager的控制, 会在关闭时候自动关闭所有由其创建的子进程

.. toctree::

  创建自己的IDE
  技术实现/index
  问题/index

.. note::

  此篇幅所有内容, 基于Theia当前版本::

    % yarn list --pattern=@theia/core
    yarn list v1.22.17
    └─ @theia/core@1.42.1
    ✨  Done in 1.06s.

一些更新
======================

跟随theia的更新,

.. theia-1.43.1
..   `@theia/core/shared/react` 下的 `Component` 接受的参数变更为两个, `React.Component<P, S>`

..   **P** 是 组件接受的类型, **S** 表示当前组件的 `state` 类型
     错了, 不是, 是编辑器的bug, 这个一直支持

theia-1.43.1
  此版本中文翻译有问题, "File" 会被翻译为本地看见, 研究代码后
  在github提出: https://github.com/eclipse-theia/theia/pull/13028

  作者有跟进

插件市场
======================

地址: https://open-vsx.org

一些常用插件:
  中文支持: https://open-vsx.org/extension/ms-ceintl/vscode-language-pack-zh-hans






