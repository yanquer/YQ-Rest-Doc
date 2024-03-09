======================================
实战-Ubuntu16下Hook系统的open
======================================

因为上一篇的 :doc:`/docs/逆向工程/实战-Mac下Hook其他进程`
失败了,
然后找原因啊, 巴拉巴拉的, 就有了这个

Hook标准库的open
======================================

.. note::

  此篇幅本也是想用add的, 但是估计是动态库的使用方式不对,
  所以最终还是换成了系统的动态库里面的open调用

  下方源码主要看open, add后面再看啥问题

test3.c源码::

  #include <stdio.h>
  #include <unistd.h>
  #include <fcntl.h>
  #include <sys/types.h>
  #include <sys/stat.h>

  int add(int a, int b){ return a+b+3; }

  int main(){
    int a = 200;
    int b = 300;
    int ret = add(a, b);
    printf("a + b = %d + %d = %d\n", a, b, ret);

    int fd = open("test3.c", O_RDONLY) ;
    if (fd != -1){
      printf("open t3 success\n");
    } else {
      printf("open t3 failed\n");
    }
    close(fd);

    return 0;
  }

编译为执行文件::

  gcc -g -o test3 test3.c

然后是hook的代码hookt3.c::

  #include "stdio.h"

  int add(int a, int b){

    printf("===hook in====");
    int ret = a + b + 100;
    printf("===hook out===");
    return ret;
  }

  extern int __open(char *,int,int);
  //打开文件
  int open(char * path,int flags,int mode)
  {
    //输出打开的文件名
    printf("=======hook open :%s\n",path);
    int ret =  __open(path,flags,mode);
    printf("===hoot fd: %d \n", ret);
    return ret;
    // return 0;
  }

编译为动态库::

  gcc -shared -fPIC  -g -o libhkt2.so hookt3.c

单独执行::

  $ ./test3
  a + b = 200 + 300 = 503
  open t3 success

加hook库::

  $ LD_PRELOAD=./libhkt2.so ./test3
  a + b = 200 + 300 = 503
  =======hook open :test3.c
  ===hoot fd: 3
  open t3 success

ldd对比下加载库顺序::

  root@740ff0ad5041:~/project/test# ldd test3
    linux-vdso.so.1 =>  (0x00007fff657c8000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f5d2fd2a000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f5d300f4000)

做了 LD_PRELOAD 的::

  root@740ff0ad5041:~/project/test# LD_PRELOAD=./libhkt2.so ldd test3
  =======hook open :/dev/tty
  ===hoot fd: 3
  =======hook open :/usr/bin/ldd
  ===hoot fd: 3
    linux-vdso.so.1 =>  (0x00007ffebd48a000)
    ./libhkt2.so (0x00007f9b745a3000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9b741d9000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f9b747a5000)
  root@740ff0ad5041:~/project/test#

为什么open要使用双下划线前缀
======================================

使用__open对底层open函数进行hook,为什么定义的函数原型是::

  extern int __open(char *,int,int);

原因是:
在GNU/Linux系统中,系统调用和库函数的名称带有前缀来区分。
对应open系统调用的库函数名称是__open。

- 如果直接使用系统调用的 API,如 open()、write() 等,定义和调用时使用的是没有下划线前缀的名称,如 open()。
- 但是如果要对系统调用做 hook,那么 hook 函数的定义需要使用下划线前缀隐藏名称,如 __open()。
- 标准库函数如 strcpy()、printf() 等,直接使用和定义时也是没有下划线前缀。
- 只有在需要进行 hook 标准库函数时,hook 函数才使用下划线前缀隐藏名称,如 __strcpy() 等。

Hook标准库的自定义的add
======================================

经过不懈努力, 终于在linux上成功了, 之前编译顺序问题导致一直失败

ub16正确编译带库的执行文件::

  gcc -o test3 test3.c -luadd -L./ -g

换个顺序就是错的::

  // error, 找不到add
  gcc -luadd -L./ -g -o test3 test3.c

自定义一个动态库, 实现add函数

add.h::

  int add(int a, int b);

add.c::

  #include "add.h"

  int add(int a, int b){
    return a+b+300;
  }

将add编译为uadd库::

  gcc -shared -fPIC -g -o libuadd.so add.c

入口执行文件test3.c::

  #include <stdio.h>
  #include <unistd.h>
  #include <fcntl.h>
  #include <sys/types.h>
  #include <sys/stat.h>
  #include "add.h"

  int main(){

    int a = 200;
    int b = 300;
    int ret = add(a, b);
    printf("a + b = %d + %d = %d\n", a, b, ret);

    int fd = open("test3.c", O_RDONLY) ;
    if (fd != -1){
      printf("open t3 success\n");
    } else {
      printf("open t3 failed\n");
    }

    close(fd);
    return 0;

  }

  // linux下  -o test3 test3.c 得在最前面, 不然找不到add
  // gcc -o test3 test3.c -luadd -L./ -g
  // gcc -g -o test3 test3.c

编译为执行文件::

  gcc -o test3 test3.c -luadd -L./ -g

hook的库源码hookt3.c::

  #include <stdio.h>

  int add(int a, int b){

    printf("===hook in add====\n");
    int ret = a + b + 100;
    printf("===hook out add===\n");
    return ret;
  }

  extern int __open(char *,int,int);
  //打开文件
  int open(char * path,int flags,int mode)
  {
    //输出打开的文件名
    printf("=======hook open :%s\n",path);
    int ret =  __open(path,flags,mode);
    printf("===hoot fd: %d \n", ret);
    return ret;
      // return 0;
  }

  // gcc -shared -fPIC  -g -o libhkt2.so hookt3.c
  // LD_LIBRARY_PATH=./ LD_PRELOAD=./libhkt2.so ./test3

编译为动态库hkt2::

   gcc -shared -fPIC  -g -o libhkt2.so hookt3.c

现在可以来测试了, 当不插入hook动态库时候::

  $ LD_LIBRARY_PATH=./ ./test3
  a + b = 200 + 300 = 800
  open t3 success

.. note::

  此处使用 LD_LIBRARY_PATH 是因为, 调用了当前自己编的动态库, 这样才能找到
  不这样的话, 要么写到系统库路径去, 要么重写下ldconf

当插入hook时::

  $ LD_LIBRARY_PATH=./ LD_PRELOAD=./libhkt2.so ./test3
  ===hook in add====
  ===hook out add===
  a + b = 200 + 300 = 600
  =======hook open :test3.c
  ===hoot fd: 3
  open t3 success

.. important::

  LD_PRELOAD 只是预加载动态库的,
  如果add直接是源码写在了执行文件, 或者add在静态库, 那么这种方法就不行了






