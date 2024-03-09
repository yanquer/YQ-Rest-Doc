=============================
一些开源便利的Git项目
=============================

alist
  文件云盘存储项目: `https://github.com/alist-org/alist/tree/main`
latest
  Mac端更新软件工具:

  官网: `https://github.com/mangerlahn/latest`

  软件旁边有个图标

  - `appStore` 图标 表示从 `AppStore` 下载安装
  - `啤酒` 图标 表示从 `HomeBrew` 下载安装
  - `小星星` 图标 表示从 `官网` 下载安装
KeyboardShortcuts
  Mac下三方库: `https://github.com/sindresorhus/KeyboardShortcuts`

  支持便捷的快捷键配置, 但是不支持配置的快捷键执行默认行为
listen1_desktop
  开源音乐播放器, 桌面版 `https://github.com/listen1/listen1_desktop`

  实际核心是一个chrome拓展, 用electron包了一下

  官网: `https://listen1.github.io/listen1/`
frida
  支持跨平台的hook, 比如侵入到一个dll内根据偏移获取内存信息

  地址: `https://github.com/frida/frida`

  Gitee地址: `https://gitee.com/wenph/frida`
frida-wechat-sticker
  地址: `https://github.com/K265/frida-wechat-sticker/tree/main`

  22年的时候可用于Windows下微信表情包提取, 现在不知道
amis
  地址: `https://github.com/baidu/amis`

  百度开源低代码框架, 前端
healthchecks
  cron 这种定时任务管理器, 是一个开源Django项目, 能在Crontab失效的时候通知

  官网: `<https://healthchecks.io>`_

  在运维中, 当你的Crontab中的任务数超过10个的时候，
  你会发现这些任务管理起来非常困难。尤其是当这些Cron任务执行失败的时候

  克隆::

    git clone https://github.com/healthchecks/healthchecks.git

  它通过一个回调接口判断你的Crontab任务有没有顺利执行。

  比如说你有一个python脚本定时执行，healthchecks给定的回调URL是::

    http://localhost:8000/ping/880cb4d

  在配置Crontab脚本的时候，就需要这么写::

    8 6 * * * python /home/user/test.py && curl -fsS -m 10 --retry 5 -o /dev/null http://localhost:8000/ping/880cb4d2

  如果未按时调用回调接口，healthchecks将会通过邮件等通知方式告警。

待处理
  - EMBY 一个媒体服务器, 介绍可看: `<https://zhuanlan.zhihu.com/p/629282288>`_


