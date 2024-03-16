========================
Map与Set
========================


.. post:: 2023-02-20 22:06:49
  :tags: ES6
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


Map 对象
========================

Map 对象保存键值对。任何值(对象或者原始值) 都可以作为一个键或一个值

Maps 和 Objects 的区别

- 一个 Object 的键只能是字符串或者 Symbols，但一个 Map 的键可以是任意值
- Map 中的键值是有序的（FIFO 原则），而添加到对象中的键则不是
- Map 的键值对个数可以从 size 属性获取，而 Object 的键值对个数只能手动计算
- Object 都有自己的原型，原型链上的键名有可能和你自己在对象上的设置的键名产生冲突

Map的迭代
-----------------------

方法一, 使用 `for ... of ...`::

  var myMap = new Map();
  myMap.set(0, "zero");
  myMap.set(1, "one");

  // 将会显示两个 log。 一个是 "0 = zero" 另一个是 "1 = one"
  for (var [key, value] of myMap) {
    console.log(key + " = " + value);
  }
  for (var [key, value] of myMap.entries()) {
    console.log(key + " = " + value);
  }
  /* 这个 entries 方法返回一个新的 Iterator 对象，它按插入顺序包含了 Map 对象中每个元素的 [key, value] 数组。 */

方法二, 使用 `forEach()`::

  var myMap = new Map();
  myMap.set(0, "zero");
  myMap.set(1, "one");

  // 将会显示两个 logs。 一个是 "0 = zero" 另一个是 "1 = one"
  myMap.forEach(function(value, key) {
    console.log(key + " = " + value);
  }, myMap)

Map 对象的操作
-----------------------

Map 与 Array的转换

Map 构造函数可以将一个二维键值对数组转换成一个 Map 对象::

  var kvArray = [["key1", "value1"], ["key2", "value2"]];
  var myMap = new Map(kvArray);

使用 Array.from 函数可以将一个 Map 对象转换成一个二维键值对数组::

  var outArray = Array.from(myMap);
  Map 的克隆
  var myMap1 = new Map([["key1", "value1"], ["key2", "value2"]]);
  var myMap2 = new Map(myMap1);

  console.log(original === clone);
  // 打印 false。 Map 对象构造函数生成实例，迭代出新的对象。

Map 的合并

合并两个 Map 对象时，如果有重复的键值，则后面的会覆盖前面的，对应值即 uno，dos， three::

  var first = new Map([[1, 'one'], [2, 'two'], [3, 'three'],]);
  var second = new Map([[1, 'uno'], [2, 'dos']]);
  var merged = new Map([...first, ...second]);

Set 对象
========================

Set 对象允许你存储任何类型的唯一值，无论是原始值或者是对象引用

Set 中的特殊值
-----------------------

Set 对象存储的值总是唯一的，所以需要判断两个值是否恒等

有几个特殊值需要特殊对待：

- +0 与 -0 在存储判断唯一性的时候是恒等的，所以不重复；
- undefined 与 undefined 是恒等的，所以不重复；
- NaN 与 NaN 是不恒等的，但是在 Set 中只能存一个，不重复。

类型转换
-----------------------

Array

Array 转 Set::

  var mySet = new Set(["value1", "value2", "value3"]);

用...操作符，将 Set 转 Array::

  var myArray = [...mySet];

String

String 转 Set::

  var mySet = new Set('hello');  // Set(4) {"h", "e", "l", "o"}
  // 注：Set 中 toString 方法是不能将 Set 转换成 String


并集::

  var a = new Set([1, 2, 3]);
  var b = new Set([4, 3, 2]);
  var union = new Set([...a, ...b]); // {1, 2, 3, 4}

交集::

  var a = new Set([1, 2, 3]);
  var b = new Set([4, 3, 2]);
  var intersect = new Set([...a].filter(x => b.has(x))); // {2, 3}

差集::

  var a = new Set([1, 2, 3]);
  var b = new Set([4, 3, 2]);
  var difference = new Set([...a].filter(x => !b.has(x))); // {1}


