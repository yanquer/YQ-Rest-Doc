====================================
wrk
====================================


.. post:: 2023-02-20 22:06:49
  :tags: linux, linux指令
  :category: 操作系统
  :author: YanQue
  :location: CD
  :language: zh-cn


轻量级性能压测工具

可以用来测试接口的性能如何,
吞吐量能达到多少,
QPS（Query per second 每秒处理完的请求数） 能达到多少呢

介绍
====================================

wrk 是一款针对 Http 协议的基准测试工具，它能够在单机多核 CPU 的条件下，
使用系统自带的高性能 I/O 机制，
如 epoll，kqueue 等，通过多线程和事件模式，对目标机器产生大量的负载。

.. note::

  wrk 是复用了 redis 的 ae 异步事件驱动框架，
  准确来说 ae 事件驱动框架并不是 redis 发明的,
  它来至于 Tcl 的解释器 jim, 这个小巧高效的框架,
  因为被 redis 采用而被大家所熟知。

优势
  - 轻量级性能测试工具;
  - 安装简单（相对 Apache ab 来说）;
  - 学习曲线基本为零，几分钟就能学会咋用了；
  - 基于系统自带的高性能 I/O 机制，
    如 epoll, kqueue, 利用异步的事件驱动框架，
    通过很少的线程就可以压出很大的并发量；
劣势
  wrk 目前仅支持单机压测，后续也不太可能支持多机器对目标机压测，
  因为它本身的定位，并不是用来取代 JMeter, LoadRunner 等专业的测试工具，
  wrk 提供的功能，对我们后端开发人员来说，应付日常接口性能验证还是比较友好的。

安装
====================================

wrk 只能被安装在类 Unix 系统上，所以我们需要一个 Linux 或者 MacOS 环境。
Windows 10 安装需要开启自带的 Ubuntu 子系统。

对于Debian::

  sudo apt-get install build-essential libssl-dev git -y
  git clone https://github.com/wg/wrk.git wrk
  cd wrk
  make
  # 将可执行文件移动到 /usr/local/bin 位置
  sudo cp wrk /usr/local/bin

对于RedHat::

  sudo yum groupinstall 'Development Tools'
  sudo yum install -y openssl-devel git
  git clone https://github.com/wg/wrk.git wrk
  cd wrk
  make
  # 将可执行文件移动到 /usr/local/bin 位置
  sudo cp wrk /usr/local/bin

对于MacOS::

  brew install wrk

对于Windows::

  Windown 10 需要在 Windows 功能 里勾选 适用于 Linux 的 Windows 子系统,
  然后通过 bash 命令切换到 Ubuntu 子系统。
  参考上面.

使用-语法
====================================

语法::

  wrk <选项> <被测HTTP服务的URL>

Options:
  -c, --connections <N>
    跟服务器建立并保持的TCP连接数量
  -d, --duration <T>
    压测时间
  -t, --threads <N>
    使用多少个线程进行压测
  -s, --script <S>
    指定Lua脚本路径
  -H, --header <H>
    为每一个HTTP请求添加HTTP头
  --latency
    在压测结束后，打印延迟统计信息
  --timeout <T>
    超时时间
  -v, --version
    打印正在使用的wrk的详细版本信息

  <N>代表数字参数，支持国际单位 (1k, 1M, 1G)
  <T>代表时间参数，支持时间单位 (2s, 2m, 2h)

.. note::

  关于线程数，并不是设置的越大，压测效果越好，线程设置过大，
  反而会导致线程切换过于频繁，效果降低，
  一般来说，推荐设置成压测机器 CPU 核心数的 2 倍到 4 倍就行了。

对 www.baidu.com 发起压力测试，
线程数为 12，模拟 400 个并发请求，持续 30 秒::

  wrk -t12 -c400 -d30s http://www.baidu.com

测试报告
====================================

还是上面的对 www.baidu.com 发起压力测试，
线程数为 12，模拟 400 个并发请求，持续 30 秒
并打印延迟报告::

  $ wrk -t12 -c400 -d30s --latency http://www.baidu.com
  Running 30s test @ http://www.baidu.com
    12 threads and 400 connections (共12个测试线程，400个连接)
			          (平均值)  (标准差)（最大值）(正负一个标准差所占比例)
    Thread Stats   Avg      Stdev     Max   +/- Stdev
      (延迟)
      Latency     1.44s   483.77ms   2.00s    76.01%
      (每秒请求数)
      Req/Sec    14.70     11.35    90.00     74.57%
    Latency Distribution (延迟分布)
      50%    1.58s
      75%    1.79s
      90%    1.92s
      99%    1.99s
    3967 requests in 30.11s, 1.55GB read  (30.11s内处理了 3967 个请求，耗费流量1.55GB)
    Socket errors: connect 158, read 0, write 0, timeout 1191 (发生错误数)
  Requests/sec:    131.77    (QPS 131.77,即平均每秒处理请求数为131.77)
  Transfer/sec:     52.60MB  (平均每秒流量52.60MB)

.. note::

  标准差啥意思？标准差如果太大说明样本本身离散程度比较高，有可能系统性能波动较大。

复杂测试
====================================

通过编写 Lua 脚本的方式，在运行压测命令时，通过参数 --script 来指定 Lua 脚本

提供的函数

function setup(thread)
  setup 函数在目标 IP 地址已经解析完, 并且所有 thread 已经生成, 但是还没有开始时被调用. 每个线程执行一次这个函数.

  setup 方法中可操作该 thread 对象，获取信息、存储信息、甚至关闭该线程::

    thread.addr             - get or set the thread's server address
    thread:get(name)        - get the value of a global in the thread's env
    thread:set(name, value) - set the value of a global in the thread's env
    thread:stop()           - stop the thread

function init(args)
  init 函数每次请求发送之前被调用.
  可以接受 wrk 命令行的额外参数. 通过 -- 指定.
function delay()
  delay函数返回一个数值, 在这次请求执行完以后延迟多长时间执行下一个请求. 可以对应 thinking time 的场景.
function request()
  request函数可以每次请求之前修改本次请求的属性. 返回一个字符串. 这个函数要慎用, 会影响测试端性能.
function response(status, headers, body)
  response函数每次请求返回以后被调用. 可以根据响应内容做特殊处理, 比如遇到特殊响应停止执行测试, 或输出到控制台等等.
function done(summary, latency, requests)
  done函数在所有请求执行完以后调用, 一般用于自定义统计结果.

wrk官网提供的setup.lua实例::

  -- example script that demonstrates use of setup() to pass
  -- data to and from the threads

  local counter = 1
  local threads = {}

  function setup(thread)
    thread:set("id", counter)
    table.insert(threads, thread)
    counter = counter + 1
  end

  function init(args)
    requests  = 0
    responses = 0

    local msg = "thread %d created"
    print(msg:format(id))
  end

  function request()
    requests = requests + 1
    return wrk.request()
  end

  function response(status, headers, body)
    responses = responses + 1
  end

  function done(summary, latency, requests)
    for index, thread in ipairs(threads) do
        local id        = thread:get("id")
        local requests  = thread:get("requests")
        local responses = thread:get("responses")
        local msg = "thread %d made %d requests and got %d responses"
        print(msg:format(id, requests, responses))
    end
  end

:参考::
  - `性能测试工具 wrk 使用教程 <https://www.cnblogs.com/quanxiaoha/p/10661650.html>`_
  - `HTTP压测工具之wrk <https://www.jianshu.com/p/ac185e01cc30>`_