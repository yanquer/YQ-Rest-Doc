=================================
wait
=================================


.. post:: 2023-02-23 23:14:15
  :tags: linux, 内置函数
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


Linux内核学习笔记 - wait、waitpid、wait3 和 wait4

Linux下有四个wait函数：

wait()
  当进程调用wait时，会暂停目前进程的执行（即阻塞），由wait() 来自动分析是否当前进程的某个子进程已退出，

  - 如果找到了一个已经变成变成僵尸进程的子进程，wait 就会收集这个子进程的信息，并将其彻底销毁后返回；
  - 如果没有找到这样一个子进程，wait 就会一直阻塞在这里，直到出现僵尸进程。


