============================
resource
============================


.. post:: 2023-02-20 22:06:49
  :tags: python, python标准库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


官网: https://docs.python.org/zh-cn/3/library/resource.html

资源使用信息

该模块提供了测量和控制程序所利用的系统资源的基本机制。

资源限制
============================

资源的使用可以通过下面描述的 setrlimit() 函数来限制。每个资源都被一对限制所控制：
一个软限制和一个硬限制。软限制是当前的限制，并且可以由一个进程随着时间的推移而降低或提高。
软限制永远不能超过硬限制。硬限制可以降低到大于软限制的任何数值，但不能提高。
（只有拥有超级用户有效UID的进程才能提高硬限制。)

可以被限制的具体资源取决于系统。它们在 man getrlimit(2) 中描述。

.. function:: resource.getrlimit(resource)

  返回一个包含 resource 当前软限制和硬限制的元组。
  如果指定了一个无效的资源，则触发 ValueError ，如果底层系统调用意外失败，则引发 error 。

.. function:: resource.setrlimit(resource, limits)¶

  设置 resource 的新的消耗极限。参数 limits 必须是一个由两个整数组成的元组 (soft, hard) ，描述了新的限制。
  RLIM_INFINITY 的值可以用来请求一个无限的限制。

  如果指定了一个无效的资源，如果新的软限制超过了硬限制，或者如果一个进程试图提高它的硬限制，将触发 ValueError 。
  当资源的硬限制或系统限制不是无限时，指定一个 RLIM_INFINITY 的限制将导致 ValueError 。
  一个有效 UID 为超级用户的进程可以请求任何有效的限制值，包括无限，
  但如果请求的限制超过了系统规定的限制，则仍然会产生 ValueError 。

  如果底层系统调用失败， setrlimit 也可能触发 error 。

  VxWorks只支持设置 RLIMIT_NOFILE 。

  触发一个 auditing event resource.setrlimit 使用参数 resource ， limits 。

.. function:: resource.prlimit(pid, resource[, limits])

  将 setrlimit() 和 getrlimit() 合并为一个函数，支持获取和设置任意进程的资源限制。
  如果 pid 为0，那么该调用适用于当前进程。 resource 和 limits 的含义与 setrlimit() 相同，只是 limits 是可选的。

  当 limits 没有给出时，该函数返回进程 pid 的 resource 限制。当 limits 被给定时，
  进程的 resource 限制被设置，并返回以前的资源限制。

  当 pid 找不到时，触发 ProcessLookupError ；当用户没有进程的 CAP_SYS_RESOURCE 时，触发 PermissionError 。

  触发一个 auditing event resource.prlimit 带有参数 pid ， resource ， limits 。

  Availability: Linux >= 2.6.36 with glibc >= 2.13.

  3.4 新版功能.
