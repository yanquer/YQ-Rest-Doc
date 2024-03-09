==================================
Python灰帽子
==================================

前言: 此文源于书籍 ``Python灰帽子``,
不过这本书有点老了, 是基于 `Python2.5` 的,
我阅读的时候尽量转换为 `Python3` 来记录.

安装相关
==================================

Python安装部分跳过. 很简单

2024推荐工具: Pycharm (原文是Eclipse, 很强但有点过时了)

最重要的库 **Ctypes**, 可参考: :doc:`/docs/后端/python/python标准库/ctypes`

Ctypes使用动态库
----------------------------------

使用 ctypes 的第一步就是明白如何解析和访问动态链接库中的函数。一个 dynamically
linked library（被动态连接的库）其实就是一个二进制文件，不过一般自己不运行，而是由别
的程序调用执行。

在 Windows 上叫做 **dynamic link libraries （DLL）动态链接库**，
在 Linux上叫做 **shared objects（SO）共享库**。无

论什么平台，这些库中的函数都必须通过导出的名字调用，
之后再在内存中找出真正的地址。所以正常情况下，要调用函数，都必须先解析出函数地址，
不过 ctypes 替我们完成了这一步。

ctypes 提供了三种方法调用动态链接库：

- cdll0
- windllO
- oledll0

它们的不同之处就在于，函数的调用方法和返回值。

- cdllO加载的库，其导出的函数必须使用标准的 cdedl调用约定。
- windI0方法加载的库，其导出的函数必须使用 stdcall调用约定（Win32API 的原生约定）
- oledl0方法和windIlO类似，不过如果函数返回一个 HRESULT错误代码，可以使用COM函数得到具体的错误信息。

调用约定
----------------------------------

调用约定专指函数的调用方法。
其中包括，函数参数的传递方法，顺序（压入栈或者传给寄存器），
以及函数返回时，栈的平衡处理。

下面这两种约定是我们最常用到的：

- **cdecl**: cdecl 调用约定，函数的参数从右往左依次压入栈内，
  函数的调用者，在函数执行完成后，负责函数的平衡。这种约定常用于x86 架构的C语言里。
- **stdcall**

**cdecl** 例子:

**InC**::

  int python_rocks（reason_one, reason_two, reason_three）；

**In x86 Assembly**::

  push reason_three
  push reason_two
  push reason_one
  call python_rocks
  add esp, 12

从上面的汇编代码中，可以清晰的看出参数的传递顺序，最后一行，栈指针增加了
12 个字节（三个参数传递个函数，每个被压入栈的指针都占 4 个字节，共12个），
使得函数调用之后的栈指针恢复到调用前的位置。

下面是个 **stdcall 调用** 约定的了例子，用于 Win32 API。

**InC**::

  int my_socks（color_one color_two, color_three）；

**In x86 Assembly**::

  push color_three
  push color_two
  push color_one
  call my_socks

这个例子里，参数传递的顺序也是从右到左，
不过栈的平衡处理由函数 my_socks自己完成，而不是调用者(没有 esp(栈顶指针) 调整指针)。

最后一点， **这两种调用方式的返回值都存储在 EAX 中** 。


构造C数据类型
----------------------------------

见 :doc:`/docs/后端/python/python标准库/ctypes`

调试器构造
==================================

白盒调试
  正常源码开发时, 利用编辑器比如Pycharm自带的调试器进行调试
黑盒调试
  不知道源码, 只知道反编译之后的汇编, 利用汇编调试工具进行调试

  一般分为

  - 用户模式: 以用户的身份;
    相关工具: WinDbg(微软生产), OllyDbg(免费程序), gdb;
    PyDbg; Immunity Debugger(界面友好, 类似OllyDbg)
  - 内核模式: 与底层交互

X86八个通用寄存器(具体说明可参考: :doc:`/docs/逆向工程/汇编`)::

  EAX, EDX, ECX, ESI, EDI, EBP, ESP 和 EBX

寄存器说明
----------------------------------

EAX 寄存器(Extended Accumulator, 扩展累加器)
  也叫做 **累加寄存器** ，除了用于存储函数的返回值外也用于执行计算的操作。
  许多优化的 x86指令集都专门设计了针对 EAX 寄存器的读写和计算指令。
  列如从最基本的加减，比较到特殊的乘除操作都有专门的EAX优化指令。

  前面我们说了，函数的返回值也是存储在EAX寄存器里。
  这一点很重要，因为通过返回的EAX 里的值我们可以判断函数是执行成功与否，或者得到确切返回值。

EDX 寄存器 (Extended Data, 扩展数据)
  也叫做数据寄存器。这个寄存器从本质上来说是EAX 寄存器的延伸，
  它辅助 EAX完成更多复杂的计算操作像乘法和除法。
  它虽然也能当作通用寄存器使用，不过更多的是结合EAX 寄存器进行计算操作。

ECX寄存器(Extended Counter, 扩展计数器)
  也叫做计数寄存器，用于循环操作，比如重复的字符存储操作，或者数字统计。
  有一点很重要，ECX寄存器的计算是向下而不是向上的（简单理解就是用于循环操作时是由大减到小的）。

  如一下Python片段::

    counter = 0
    while counter < 10:
      print(counter)
      counter += 1

  如果你把这代码转化成汇编代码，你会看到第一轮的时候ECX 将等于 10，
  第二轮的时候等于9，如此反复知道ECX 减少到0。
  这很容易让人困惑，因这和 Python 的循环刚好代码相反，但是只要记得ECX 是向下计算的就行了。

  在x86汇编里，依靠 ESI 和 EDI 寄存器能对需要循环操作的数据进行高效的处理。

ESI 寄存器(Extended Source Index, 扩展源索引)
  是源操作数指针，存储着输入的数据流的位置。
  ESI （source index）用于读
EDI 寄存器(Extended Destination Index, 扩展目标索引)
  是目的操作数指针，存储了计算结果存储的位置。
  EDI （destination index）用于写。

  用源操作数指针和目的操作数指针，极大的提高了程序处理数据的效率。

ESP(Extended Stack Pointer, 扩展堆栈指针) 和 EBP(Extended Base Pointer, 扩展基址指针)
  分别是栈指针和基指针.
  这两个寄存器共同负责函数的调用和栈的操作。
  当一个函数被调用的时候，函数需要的参数被陆续压进栈内最后函数的返回地址也被压进。
  ESP指着栈顶，也就是返回地址。
  EBP 则指着栈的底端。有时候，编译器能够做出优化，释放EBP，使其不再用于栈的操作，只作为普通的寄存器使用。

EBX(Extended Base, 扩展基址)
  唯一一个没有特用途的寄存器。它能够作额外的数据储存器。

EIP(Extended Instruction Pointer, 扩展指令指针)
  总是指向马上要执行的指令。
  当CPU执行一个程序的成千上万的代码的时候，EIP 会实时的指向当前CPU马上要执行到的位置。

一个调试器必须能够很方便的获取和修改这些寄存器的内容。
每一个操作系统都提供了一个接口让调试器和 CPU 交互，以便能够获取和修改这些值。

.. note::

  - a(Accumulator), 8位累加器。8080。b 基址，c 计数，d数据
  - ax(Accumulator)，16位累加器，由ah，al 组成。8086。bx=bh+bl,cx=ch+cl,dx=dh+dl
  - eax(Extended Accumulator)，32位累加器，80386
  - rax(Return Accumulator)，64位累加器。X86-64

  关于X的解释::

    最早的x86的累加寄存器叫ax, 高位為ah, 低位為al, 拼在一起叫ax.
    IA-32時代以后叫eax, 擴展(extend)為32位, 這個e就是extend, a是accumulate, x其實是h加l的意思, 沒特別意義

  参考: `<http://bbs.chinaunix.net/thread-2315852-1-1.html>`_

栈
----------------------------------

机器执行计算是通过栈进行操作的,
**ESP** 总是指向栈顶, **EBP** 指向栈基址

栈从内存高地址向低地址增长

断点
----------------------------------

- 软件断点: ``INT3`` 中断
- 硬件断点: ``INT1`` 中断
- 内存断点: 利用保护页(可读, 可写, 可执行页)

实现一个Windows调试器
==================================

进程启动方式(两种)

- 由调试器启动进程
- 调试器附加到进程

相关Win32API:

启动进程::

  BOOL WINAPI Create ProcessA(
    LPCSTR IpApplicationName,
    LPTSTR IpCommandLine,
    LPSECURITY_ATTRIBUTES IpProcessAttributes,
    LPSECURITY_ATTRIBUTES IpThreadAttributes,
    BOOL bInheritHandles,
    DWORD dwCreationFlags,
    LPVOID IpEnvironment,
    LPCTSTR IpCurrentDirectory,
    LPSTARTUPINFO IpStartupInfo,
    LPPROCESS_INFORMATION IpProcessInformation
  )

附加到进程前的打开进程句柄::

  HANDLE WINAPI OpenProcess(
    DWORD dwDesiredAccess,
    BOOL bInheritHandle
    DWORD dwProcessId
  )

附加到进程::

  BOOL WINAPI DebugActiveProcess(
    DWORD dwProcessId
  )




