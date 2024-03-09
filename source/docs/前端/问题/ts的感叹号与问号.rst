======================
ts的!与?
======================

表示变量可能为空.

!用法
======================

用在变量前表示取反

用在赋值的内容后时，使null和undefined类型可以赋值给其他类型并通过编译，表示该变量值可空

?用法
======================

可以表示可选参数

如::

  interface IDemo {
      x?: number
  }

可防御性编程::

  const a = fetch(...) || {}		// 假设a是从后端拿到的一个对象类型数据
  const unsafeData = a.b.c		// 这样写时不安全的，无法确保b是否有值，如果为空则b.c会进行报错
  const safeData = a?.b?.c		// 实际上就是相当于 const safeData = a && a.b && a.b.c

其他见 :doc:`/docs/前端/typescript/问号与叹号`

