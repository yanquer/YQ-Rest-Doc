===========================
vscode不同文件配置不同缩进
===========================


.. post:: 2024-03-09 18:21:01
  :tags: vscode
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


Command + Shift + P 打开用户设置, 参考以下设置::

  "[restructuredtext]": {
    // "editor.detectIndentation": false,
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
  },

一开始用的 ``rst`` 和 ``reStructuredText`` 都失败了.
最后去setting.json联想输入才知道是 ``restructuredtext`` (小写)


