====================================
Reflect 与 Proxy
====================================

https://www.runoob.com/w3cnote/es6-reflect-proxy.html

即反射与代理

Proxy
====================================

Proxy 可以对目标对象的读取、函数调用等操作进行拦截，然后进行操作处理.
它不直接操作对象，而是像代理模式，通过对象的代理对象进行操作，在进行这些操作时，可以添加一些需要的额外操作。

用法::

  let proxy = new Proxy(target, handler)

- target: 需要代理的源对象
- handler: 代理处理操作, 若为空即不做代理拦截处理

对象代理用例::

  let target = {
      name: 'Tom',
      age: 24
  }
  let handler = {
      get: function(target, key) {
          console.log('getting '+key);
          return target[key]; // 不是target.key
      },
      set: function(target, key, value) {
          console.log('setting '+key);
          target[key] = value;
      }
  }
  let proxy = new Proxy(target, handler)
  proxy.name     // 实际执行 handler.get
  proxy.age = 25 // 实际执行 handler.set
  // getting name
  // setting age
  // 25

实例方法

.. function:: get(target, propKey, receiver)

  receiver
    接收着, 一般表示代理对象, 比如上面的proxy

.. function:: set(target, propKey, value, receiver)

.. function:: apply(target, ctx, args)

  用于拦截函数的调用、call 和 reply 操作

  target
    目标对象
  ctx
    目标对象上下文
  args
    目标对象的参数数组

.. function:: has(target, propKey)

  用于拦截 HasProperty 操作，即在判断 target 对象是否存在 propKey 属性时，会被这个方法拦截.
  此方法不判断一个属性是对象自身的属性，还是继承的属性

.. function:: construct(target, args)

  用于拦截 new 命令。返回值必须为对象

.. function:: deleteProperty(target, propKey)

  用于拦截 delete 操作，如果这个方法抛出错误或者返回 false ，propKey 属性就无法被 delete 命令删除

.. function:: defineProperty(target, propKey, propDesc)

  用于拦截 Object.definePro若目标对象不可扩展，增加目标对象上不存在的属性会报错;
  若属性不可写或不可配置，则不能改变这些属性

  其实就是拦截对象属性定义, 比如 `ob.name=tom`

erty 操作

.. function:: getOwnPropertyDescriptor(target, propKey)

  用于拦截 Object.getOwnPropertyD() 返回值为属性描述对象或者 undefined 。

ptor 属性

.. function:: getPrototypeOf(target)

  主要用于拦截获取对象原型的操作。包括以下操作：

  - Object.prototype._proto_
  - Object.prototype.isPrototypeOf()
  - Object.getPrototypeOf()
  - Reflect.getPrototypeOf()
  - instanceof

  注意，返回值必须是对象或者 null ，否则报错.
  另外，如果目标对象不可扩展（non-extensible），getPrototypeOf 方法必须返回目标对象的原型对象

.. function:: isExtensible(target)

  用于拦截 Object.isExtensible 操作。
  该方法只能返回布尔值，否则返回值会被自动转为布尔值。

.. function:: ownKeys(target)

  用于拦截对象自身属性的读取操作。主要包括以下操作:

  - Object.getOwnPropertyNames()
  - Object.getOwnPropertySymbols()
  - Object.keys()
  - or...in

  方法返回的数组成员，只能是字符串或 Symbol 值，否则会报错。

  若目标对象中含有不可配置的属性，则必须将这些属性在结果中返回，否则就会报错。

  若目标对象不可扩展，则必须全部返回且只能返回目标对象包含的所有属性，不能包含不存在的属性，否则也会报错。

.. function:: preventExtensions(target)

  拦截 Object.preventExtensions 操作。
  该方法必须返回一个布尔值，否则会自动转为布尔值。

.. function:: setPrototypeOf

  主要用来拦截 Object.setPrototypeOf 方法。
  返回值必须为布尔值，否则会被自动转为布尔值。
  若目标对象不可扩展，setPrototypeOf 方法不得改变目标对象的原型。

.. function:: Proxy.revocable()

  用于返回一个可取消的 Proxy 实例。

Reflect
====================================

Reflect 可以用于获取目标对象的行为，它与 Object 类似，但是更易读，为操作对象提供了一种更优雅的方式.
它的方法与 Proxy 是对应的。

ES6 中将 Object 的一些明显属于语言内部的方法移植到了 Reflect 对象上（当前某些方法会同时存在于 Object 和 Reflect 对象上），
未来的新方法会只部署在 Reflect 对象上。

Reflect 对象对某些方法的返回结果进行了修改，使其更合理。
Reflect 对象使用函数的方式实现了 Object 的命令式操作。

静态方法

.. function:: Reflect.get(target, name, receiver)

  查找并返回 target 对象的 name 属性。

Reflect.set(target, name, value, receiver)
将 target 的 name 属性设置为 value。返回值为 boolean ，true 表示修改成功，false 表示失败。当 target 为不存在的对象时，会报错。

.. function:: Reflect.has(obj, name)

  是 name in obj 指令的函数化，用于查找 name 属性在 obj 对象中是否存在。返回值为 boolean。如果 obj 不是对象则会报错 TypeError。

.. function:: Reflect.deleteProperty(obj, property)

  是 delete obj[property] 的函数化，用于删除 obj 对象的 property 属性，返回值为 boolean。如果 obj 不是对象则会报错 TypeError。

.. function:: Reflect.construct(obj, args)

  等同于 new target(...args)。

.. function:: Reflect.getPrototypeOf(obj)

  用于读取 obj 的 _proto_ 属性。在 obj 不是对象时不会像 Object 一样把 obj 转为对象，而是会报错。

.. function:: Reflect.setPrototypeOf(obj, newProto)

  用于设置目标对象的 prototype。

.. function:: Reflect.apply(func, thisArg, args)

  等同于 Function.prototype.apply.call(func, thisArg, args)

  func
    目标函数；
  thisArg
    目标函数绑定的 this 对象；
  args
    目标函数调用时传入的参数列表，可以是数组或类似数组的对象.
    若目标函数无法调用，会抛出 TypeError

.. function:: Reflect.defineProperty(target, propertyKey, attributes)

  用于为目标对象定义属性。如果 target 不是对象，会抛出错误。

.. function:: Reflect.getOwnPropertyDescriptor(target, propertyKey)

  用于得到 target 对象的 propertyKey 属性的描述对象。在 target 不是对象时，会抛出错误表示参数非法，不会将非对象转换为对象。

.. function:: Reflect.isExtensible(target)

  用于判断 target 对象是否可扩展。返回值为 boolean 。如果 target 参数不是对象，会抛出错误

.. function:: Reflect.preventExtensions(target)

  用于让 target 对象变为不可扩展。如果 target 参数不是对象，会抛出错误

.. function:: Reflect.ownKeys(target)

  用于返回 target 对象的所有属性，等同于 Object.getOwnPropertyNames 与Object.getOwnPropertySymbols 之和


