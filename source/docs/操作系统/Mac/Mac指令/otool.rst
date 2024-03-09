=======================
otool
=======================

某种程度上可以看作 :doc:`/docs/操作系统/linux/linux指令/ldd` 的替代,
因为Mac上没有 ldd 指令.

iOS应用所依赖的系统库检查

otool(object file displaying tool)
  针对目标文件的展示工具，用来发现应用中使用到了哪些系统库，调用了其中哪些方法，
  使用了库中哪些对象及属性，它是Xcode自带的常用工具。

常用的命令::

  -f print the fat headers
  -a print the archive header
  -h print the mach header
  -l print the load commands
  -L 打印用到的 shared libraries, 就是看用到了哪些动态库
  -D print shared library id name
  -t 打印汇编的text段, 一般需要与-v一起使用(the text section (disassemble with -v))
  -p <routine name>  start dissassemble from routine name
  -s <segname> <sectname> print contents of section
  -d print the data section
  -o print the Objective-C segment
  -r print the relocation entries
  -S print the table of contents of a library
  -T print the table of contents of a dynamic shared library
  -M print the module table of a dynamic shared library
  -R print the reference table of a dynamic shared library
  -I print the indirect symbol table
  -H print the two-level hints table
  -G print the data in code table
  -v print verbosely (symbolically) when possible
  -V 打印反汇编符号操作数(disassembled operands symbolically)
  -c print argument strings of a core file
  -X print no leading addresses or headers
  -m don't use archive(member) syntax
  -B force Thumb disassembly (ARM objects only)
  -q use llvm's disassembler (the default)
  -Q use otool(1)'s disassembler
  -mcpu=arg use `arg' as the cpu for disassembly
  -j print opcode bytes
  -P print the info plist section as strings
  -C print linker optimization hints
  --version print the version of /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/otool







