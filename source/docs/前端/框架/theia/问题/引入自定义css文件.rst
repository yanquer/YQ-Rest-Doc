=============================
引入自定义css文件
=============================


.. post:: 2024-03-08 23:31:08
  :tags: 框架, theia, 问题
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


在拓展根目录(src)下的 `browser` 下新建一个 `style` 文件夹,
其中新建自己的css, 如 `my-style.css`

如果没有定义前端服务, 直接在扩展的 `package.json` 中配置::

  "theiaExtensions": [
    {
      "frontend": "lib/browser/style/my-style.css"
    }
  ]

如果有定义前端服务如 `index.ts`, 那么 `package.json` 中已经有::

  "theiaExtensions": [
    {
      "frontend": "lib/browser/index"
    }
  ]

这个时候只需要简单的在 `index.ts` 导入即可::

  import '../../src/browser/style/my-style.css'

因为lib是编译的, 下面没有css, 所以得从根目录重新进

.. note::

  如果是覆盖theia框架原有的, 不用导

