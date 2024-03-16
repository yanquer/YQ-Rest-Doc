========================
child_process
========================


.. post:: 2023-02-20 22:06:49
  :tags: node, 标准库
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


:官网::
    `Child Process <https://nodejs.org/docs/latest-v10.x/api/child_process.html>`_

子进程操作相关模块

创建子进程方式:

- `spawn`_ :  启动一个子进程来执行命令；
- `exec`_  :  启动一个子进程来执行命令，与 `spawn`_ 不同的是，它有一个回调函数获知子进程的状况；
- `execFile`_ : 启动一个子进程来执行可执行文件；
- `fork`_  :  与 `spawn`_ 类似，不同点在于它创建 Node 的子进程只需指定要执行的 JavaScript 文件模块即可；

.. note::

    `exec`_ , `execFile`_ , `fork`_ 底层都是通过 `spawn`_ 实现

spawn
========================

.. function:: child_process.spawn(command[, args][, options])

    command: string
        要执行的命令, 实际还是可执行文件；
    args: string[]
        字符串参数列表；
    options: {}
        argv0: string
            显式地设置发送给子进程的 argv[0] 的值， 如果没有指定，则会被设置为 command 的值；
        detached: Boolean
            让子进程独立于父进程之外运行；

        其他: options_

exec
========================

.. function:: child_process.exec(command[, options][, callback])

    创建一个 shell，然后在 shell 里执行命令。执行完成后，将 stdout、stderr 作为参数传入回调方法

    options支持参数:

    - cwd: 当前工作路径；
    - env: 环境变量；
    - encoding: 编码，默认是 utf8；
    - shell: 用来执行命令的 shell，unix 上默认是 /bin/sh，windows 上默认是 cmd.exe；
    - timeout: 默认是 0；当子进程运行超过 timeout 毫秒，那么，就会给进程发送 killSignal 指定的信号（比如 SIGTERM）
    - killSignal: 默认是 SIGTERM；
    - uid: 执行进程的 uid；
    - gid: 执行进程的 gid；
    - maxBuffer:  标准输出、错误输出最大允许的数据量（单位为字节），如果超出的话，子进程就会被杀死；默认是 200*1024（即 200k ）

基本使用::

    const {exec} = require('child_process');

    exec('ls', (error, stdout, stderr) => {
        // do ...
    });

其中, ``(error, stdout, stderr)`` 对应类型如下::

    error: ExecException | null,
            // ExecException只是一个接口, 通用属性有四个:
            // cmd?: string | undefined;
            // killed?: boolean | undefined;
            // code?: number | undefined;
            // signal?: NodeJS.Signals | undefined;
    stdout: str,
    stderr: str,

高级一点用法, 对输出进行监听::

    exec('ls').stdout.on('data', data => {
        console.log(data);
    });

execFile
========================

.. function:: child_process.execFile(file[, args][, options][, callback])

    跟 `exec`_ 类似，不同点在于，没有创建一个新的 shell，options 参数与 `exec`_ 一样

    file: string

        实际是可执行文件, 比如 ping, ls

    options: options_

例::

    const child_process = require('child_process');

    child_process.execFile('ls', ['./'], (error, stdout, stderr) => {
        /// do ...
        console.log(error, stdout, stderr);
    });

fork
========================

.. function:: child_process.fork(modulePath[, args][, options])

    modulePath: string | URL
        子进程运行的模块；
    args: string[]
        字符串参数列表；
    options: {}
        支持的参数列表, 有以下参数, 基本与 `spawn`_ 一致

        .. _options:

        cwd: str
            当前工作路径；
        detached: boolean
            让子进程独立于父进程之外运行；
        env: object
            环境变量；
        execArgv: string[]
            传给可执行文件的字符串参数列表。默认是 process.execArgv，跟父进程保持一致；
        execPath: string
            用来创建子进程的可执行文件，默认是 /usr/local/bin/node。也就是说，你可通过 execPath 来指定具体的 node 可执行文件路径；（比如多个 node 版本）
        gid: number
            执行进程的 gid；
        killSignal: string|number
            默认是 SIGTERM；
        serialization: string
            序列化
        signal: AbortSingal
            .
        silent: boolean
            默认是 false，即子进程的 stdio 从父进程继承。如果是 true，则直接 pipe 向子进程的child.stdin、child.stdout 等；
        stdio: Any[] | string
            选项用于配置在父进程和子进程之间建立的管道，如果声明了 stdio，则会覆盖 silent 选项的设置；

            如父子进程共用一个输出管道::

                stdio: 'inherit'

        timeout: number
            默认是 0；当子进程运行超过 timeout 毫秒，那么，就会给进程发送 killSignal 指定的信号（比如 SIGTERM）
        uid: number
            执行进程的 uid；

支持的事件
========================

- close 事件: 子进程的 ``stdio`` 流关闭时触发；
- disconnect 事件: 事件在父进程手动调用 ``child.disconnect`` 函数时触发；
- error 事件: 产生错误时会触发；
- exit 事件: 子进程自行退出时触发；
- message 事件: 它在子进程使用 ``process.send()`` 函数来传递消息时触发；

事件使用 on 调用::

    exec('ls').stdout.on('exit', (code, signal) => {
        console.log(code);
    });
