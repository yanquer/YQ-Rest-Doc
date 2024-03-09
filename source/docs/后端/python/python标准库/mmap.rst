=======================
mmap
=======================

:官网文档::
  `mmap - 内存映射文件支持 <https://docs.python.org/zh-cn/3/library/mmap.html>`_

:部分参考::
  `Python多进程（2）——mmap模块与mmap对象 <https://www.cnblogs.com/Security-Darren/p/4733387.html>`_

创建内存映射的文件对象. 类似于file打开的文件对象的操作, 同时又支持了字节数组的一些操作如切片.

通俗来说就是创建一个存在于内存的文件(个人观点).

与 string 的区别是:

- mmap 对象不提供字符串对象的方法；
- mmap 对象是可变的, 而 str 对象是不可变的
- mmap 对象同时对应于打开的文件, 多态于一个Python file 对象
- mmap 对象可以切片和索引, 也可以为它的切片或索引赋值（因为 mmap 对象是可变的）,
  为 mmap 对象的切片赋值时, 赋值语句右值的长度必须和左值切片的长度相同.
  mmap 对象可以作为进程间通过文件进行 IPC 的一种替换手段.

mmap类
=======================

定义
-----------------------

**windows版本**

.. class:: class mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT[, offset])

**unix版本**

.. class:: class mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset])

参数
-----------------------

fileno:
  文件描述符(句柄), 可以是 ``-1`` 这种, 也可以 ``open().fileno()``
length: int
  将指定 fileno 的前 length 字节映射到内存.
  映射的内容字节长度, 为0则表示映射整个文件.

  - 如果 length 大于当前文件大小, 则文件将扩展为包含 length 个字节.
  - 如果 length 为 0, 则映射的最大长度为当前文件大小.
  - 如果文件为空,  Windows 会引发异常（你无法在Windows上创建空映射）.
tagname=None
  `platform: windows`. 如果 tagname 被指定且不是 None , 则是为映射提供标签名称的字符串(为一段内存映射指定名称).
  Windows 允许你对同一文件拥有许多不同的映射(一个文件上面可以同时具有多个 mmap).

  .. windows中的内存映射都是可读可写的, 同时在进程之间共享.

  - 如果指定现有标签的名称, 则会打开该标签, 否则将创建该名称的新标签.
  - 如果省略此参数或设置为 None , 则创建的映射不带名称.

  避免使用 tag 参数将有助于使代码在Unix和Windows之间可移植.
flags=MAP_SHARED
  `platform: unix`. flags 指明映射的性质.

  - MAP_PRIVATE 会创建私有的写入时拷贝映射, 因此对 mmap 对象内容的修改将为该进程所私有.
  - MAP_SHARED 会创建与其他映射同一文件区域的进程所共享的映射.  默认值为 MAP_SHARED.
prot=PROT_WRITE|PROT_READ
  `platform: unix`. 如果指明了 prot, 它将给出所需的内存保护方式；
  最有用的两个值是 PROT_READ 和 PROT_WRITE,
  分别指明页面为可读或可写. prot 默认为 PROT_READ | PROT_WRITE (可读可写).
access=ACCESS_DEFAULT[, offset])
  在unix下, 可以指定 access 作为替代 flags 和 prot 的可选关键字形参.
  同时指定 flags, prot 和 access 将导致错误.

  对于所有平台:

  可以将 access 指定为可选的关键字参数.  access 接受以下四个值之一:

  - ACCESS_READ 指定只读. 向 ACCESS_READ 内存映射赋值会引发 TypeError 异常.
  - ACCESS_WRITE 指定只写. 向 ACCESS_WRITE 内存映射赋值会影响内存和底层的文件.
  - ACCESS_COPY 指定写时复制内存. 向 ACCESS_COPY 内存映射赋值会影响内存, 但不会更新底层的文件.
  - ACCESS_DEFAULT 推迟到 prot

  access 可以在 Unix 和 Windows 上使用. 如果未指定 access , 则 Windows mmap 返回只写映射.
  这三种访问类型的初始内存值均取自指定的文件.

  offset 可以被指定为非负整数偏移量.  mmap 引用将相对于从文件开头的偏移.

  offset 默认为0.  offeset 必须是 ALLOCATIONGRANULARITY 的倍数.

注意::

  创建 mmap 将会引发一个 审计事件 mmap.__new__ 附带参数 fileno, length, access, offset.

mmap 对象的方法
=======================

.. function:: close()

  关闭 mmap。 后续调用该对象的其他方法将导致引发 ValueError 异常。 此方法将不会关闭打开的文件。

.. function:: closed

  如果文件已关闭则返回 True。

.. function:: find(sub[, start[, end]])
  :noindex:

  返回子序列 sub 在对象内被找到的最小索引号，使得 sub 被包含在 [start, end] 范围中。 可选参数 start 和 end 会被解读为切片表示法。 如果未找到则返回 -1。

  在 3.5 版更改: 现在接受可写的 字节类对象。

.. function:: flush([offset[, size]])

  将对文件的内存副本的修改刷新至磁盘。 如果不使用此调用则无法保证在对象被销毁前将修改写回存储。 如果指定了 offset 和 size，则只将对指定范围内字节的修改刷新至磁盘；在其他情况下，映射的全部范围都会被刷新。 offset 必须为 PAGESIZE 或 ALLOCATIONGRANULARITY 的倍数。

  返回 None 以表示成功。 当调用失败时将引发异常。

  在 3.8 版更改: 在之前版本中，成功时将返回非零值；在 Windows 下当发生错误时将返回零。 在 Unix 下 成功时将返回零值；当发生错误时将引发异常。

.. function:: madvise(option[, start[, length]])

  将有关内存区域的建议 option 发送至内核，从 start 开始扩展 length 个字节。 option 必须为系统中可用的 MADV_* 常量 之一。 如果省略 start 和 length，则会包含整个映射。 在某些系统中（包括 Linux），start 必须为 PAGESIZE 的倍数。

  可用性: 具有 madvise() 系统调用的系统。

  3.8 新版功能.

.. function:: move(dest, src, count)

  将从偏移量 src 开始的 count 个字节拷贝到目标索引号 dest。 如果 mmap 创建时设置了 ACCESS_READ，则调用 move 将引发 TypeError 异常。

.. function:: read([n])

  返回一个 bytes，其中包含从当前文件位置开始的至多 n 个字节。 如果参数省略，为 None 或负数，则返回从当前文件位置开始直至映射结尾的所有字节。 文件位置会被更新为返回字节数据之后的位置。

  在 3.3 版更改: 参数可被省略或为 None。

.. function:: read_byte()

  将当前文件位置上的一个字节以整数形式返回，并让文件位置前进 1。

.. function:: readline()

  返回一个单独的行，从当前文件位置开始直到下一个换行符。 文件位置会被更新为返回字节数据之后的位置。

.. function:: resize(newsize)

  改变映射以及下层文件的大小，如果存在的话。 如果 mmap 创建时设置了 ACCESS_READ 或 ACCESS_COPY，则改变映射大小将引发 TypeError 异常。

  On Windows: Resizing the map will raise an OSError if there are other maps against the same named file. Resizing an anonymous map (ie against the pagefile) will silently create a new map with the original data copied over up to the length of the new size.

  在 3.11 版更改: Correctly fails if attempting to resize when another map is held Allows resize against an anonymous map on Windows

.. function:: rfind(sub[, start[, end]])

  返回子序列 sub 在对象内被找到的最大索引号，使得 sub 被包含在 [start, end] 范围中。 可选参数 start 和 end 会被解读为切片表示法。 如果未找到则返回 -1。

  在 3.5 版更改: 现在接受可写的 字节类对象。

.. function:: seek(pos[, whence])

  设置文件的当前位置。 whence 参数为可选项并且默认为 os.SEEK_SET 或 0 (绝对文件定位)；其他值还有 os.SEEK_CUR 或 1 (相对当前位置查找) 和 os.SEEK_END 或 2 (相对文件末尾查找)。

.. function:: size()

  返回文件的长度，该数值可以大于内存映射区域的大小。

.. function:: tell()

  返回文件指针的当前位置。

.. function:: write(bytes)

  将 bytes 中的字节数据写入文件指针当前位置的内存并返回写入的字节总数 (一定不小于 len(bytes)，因为如果写入失败，将会引发 ValueError)。 在字节数据被写入后文件位置将会更新。 如果 mmap 创建时设置了 ACCESS_READ，则向其写入将引发 TypeError 异常。

  在 3.5 版更改: 现在接受可写的 字节类对象。

  在 3.6 版更改: 现在会返回写入的字节总数。

.. function:: write_byte(byte)

  将整数值 byte 写入文件指针当前位置的内存；文件位置前进 1。 如果 mmap 创建时设置了 ACCESS_READ，则向其写入将引发 TypeError 异常。

对于EOF的处理, write() 和 read_byte() 抛出异常 ValueError, 而 write_byte() 和 read() 什么都不做.






