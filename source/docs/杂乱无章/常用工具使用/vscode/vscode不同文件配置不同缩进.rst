===========================
vscode不同文件配置不同缩进
===========================

Command + Shift + P 打开用户设置, 参考以下设置::

  "[restructuredtext]": {
    // "editor.detectIndentation": false,
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
  },

一开始用的 ``rst`` 和 ``reStructuredText`` 都失败了.
最后去setting.json联想输入才知道是 ``restructuredtext`` (小写)


