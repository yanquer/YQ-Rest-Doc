====================================
sudo与su的部分说明
====================================


.. post:: 2024-02-21 21:55:17
  :tags: linux, 概念性
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


- su <user>: 切换到指定的user, 输出这个user的密码. 可以加 ``-`` 指定切换到user的环境.
- sudo <cmd>: 以root的身份执行指令, 还是使用当前用户的环境, 可以使用 ``-u`` 指定其他用户
- sudo su: 切换到root, 保留最初的用户环境
- sudo su -: 切换到root, 同时存在最初的用户的环境与root的用户环境, 如果冲突, 以root为准

