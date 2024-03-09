=============================
electron生命周期
=============================

退出的两个调用:

- app.quit(): 尝试关闭所有窗口(如果窗口有 window.on('close', (e) => e.preventDefault()) 则失败)
  - 首先发出 before-quit 事件，如果所有窗口关闭成功，则发出 will-quit 事件，然后 app 退出
  - 此方法会确保执行所有的 beforeunload 和 unload（dom）事件，当然可以在 beforeunload 事件中返回 false 阻止继续退出。
- app.exit([code]): 使用 exitCode 立即退出。exitCode 默认为0
  - 所有窗口立即关闭，而不询问用户，且不触发 beforeunload 和 unload 事件





