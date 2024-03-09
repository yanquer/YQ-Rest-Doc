=============================
DYLD_PRINT_LIBRARIES
=============================

设置值为1后, 执行程序之前会打印出运行时加载的所有动态库

用例::

  $ DYLD_PRINT_LIBRARIES=1 ./test2

  // 这部分是运行时加载的动态库, 篇幅较长, 此处只截取头尾
  dyld[43741]: <DD3BA6F6-FA28-3A28-AA7D-F95D176C25B3> /Users/yanque/project/code/TryTest/test2
  dyld[43741]: <683DEB82-6E72-394B-945D-AB3A1A8BE1D8> /Users/yanque/project/code/TryTest/libtest2preutil.dylib
  ...
  dyld[43741]: <6F11E645-DB1C-325D-AC28-91740663E4DD> /usr/lib/system/libxpc.dylib
  dyld[43741]: <7E3B4177-738A-305C-93AA-D9E395B96B9D> /usr/lib/libobjc.A.dylib
  dyld[43741]: <87B41A1F-8387-3AF3-BB41-C86D4B6A21A5> /usr/lib/liboah.dylib

  // 下面是执行结果
  a + b + 随机值= 10000 + 10090 + 3 = 0
  交换a, b的值, 交换前: a: 10000; b: 10090
  交换a, b的值, 交换后: a: 10090; b: 10000





