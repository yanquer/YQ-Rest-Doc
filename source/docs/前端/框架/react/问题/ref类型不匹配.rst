======================================
ref类型不匹配
======================================


.. post:: 2024-03-07 22:13:39
  :tags: 框架, react, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


大致报错信息::

  MutableRefObject<SelectComponent | undefined> is not assignable to type Ref<SelectComponent> | undefined

或者::

  Type ForwardedRef<unknown> is not assignable to type LegacyRef<SelectComponent> | undefined

原因:

.. 如果在将 ref 传递给类组件时收到类型错误，可能是因为 ref 的类型不匹配。

在 React 中，ref 可以是两种类型之一：LegacyRef 或 MutableRefObject。

- LegacyRef 是一个旧版本的 ref 类型，适用于类组件和函数组件。
- MutableRefObject 是一个较新的 ref 类型，适用于函数组件和 React Hooks。
  如果你在函数组件中使用 useRef() 创建 ref，那么你得到的是 MutableRefObject 类型的对象。

  但是，类组件中的 ref 应该是 LegacyRef 类型。

这个时候需要将其转换一下, 比如::

  import {SelectComponent, SelectComponentProps} from "@theia/core/lib/browser/widgets/select-component"
  import * as React from "react";

  const ForwardedChildComponent = React.forwardRef((props: SelectComponentProps, ref) => {
      return <SelectComponent {...props} ref={ref as React.RefObject<SelectComponent>} />;
  });



