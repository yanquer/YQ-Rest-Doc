==================================
ssh重置计数器
==================================


.. post:: 2023-02-23 00:00:02
  :tags: linux, 问题
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


这里是指, 登陆失败时, ssh会统计次数,
超过时, 会等待一段时间才可以再次继续.

可以使用 :ref:`PAM_RESET_USER` 来重置这个计数器, 以立刻继续使用


