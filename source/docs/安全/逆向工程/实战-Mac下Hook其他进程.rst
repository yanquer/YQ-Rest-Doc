===============================
实战-Mac下Hook其他进程
===============================


.. post:: 2024-03-09 18:21:01
  :tags: 逆向工程
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


写一个测试的源码test2.cpp::

  #include "stdio.h"

  int add(int a, int b){
    int tmp = a + 3;
    return tmp + b;
  }

  extern "C"{
    int add2(int a, int b){ return a+b+10;}
  }

  int sub(int a, int b){
    return a-b;
  }

  void swap(int *a, int *b){
    int *tmp;
    *tmp = *a;
    *a = *b;
    *b = *tmp;
  }

  int main(){

    int a = 10000;
    int b = 10090;
    int c = 10000;
    int d = 10000;

    int e[] = {10000, 10000, 5, 80};
    int f[] = {10000, 5, 10000, 80};

    int retAdd = add(a, b);
    printf("a + b + 随机值= %d + %d + 3 = %d\n", a, b, retAdd);

    printf("交换a, b的值, 交换前: a: %d; b: %d\n", a, b);
    swap(&a, &b);
    printf("交换a, b的值, 交换后: a: %d; b: %d \n", a, b);

    // fflush();
    return 0;

  }

将其编译为执行文件test2::

  // g++ -std=c++11 -dynamiclib -g -o libtest2.dylib test2.cpp
  // g++ -std=c++11 -g -l test2preutil -L /Users/yanque/project/code/TryTest  -o test2 test2.cpp
  /usr/bin/clang++ -std=gnu++14 -fcolor-diagnostics -fansi-escape-codes -g test2.cpp -o test2

编码钩子test2-hook-add-func.cpp::

  #include "stdio.h"
  #include <dlfcn.h>
  #include <stdio.h>
  #include <stdlib.h>

  // 定义原始函数指针类型
  typedef int (*OrigAddFunc)(int a, int b);

  int add(int a, int b)
  {
      OrigAddFunc orig_add = NULL;
      orig_add = (OrigAddFunc)dlsym(RTLD_NEXT,"_Z3addii");
      int tmp = orig_add(a, b);
      fprintf(stderr, "hook add; a + b = %d + %d = %d", a, b, tmp);
      fprintf(stderr, "%s %d %d\n", __FILE__, __LINE__, tmp);
      return tmp;
  }

编译为动态库 `libtest2hook.dylib`::

   g++ -std=c++11 -dynamiclib -o libtest2hook.dylib test2-hook-add-func.cpp

因为是Mac系统::

  DYLD_INSERT_LIBRARIES=`pwd`/libtest2hook.dylib ./test2

Linux环境变量是 ``LD_PRELOAD``


