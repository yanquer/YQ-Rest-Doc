===============================
electron-builder配置生成位置
===============================


.. post:: 2023-02-26 21:30:12
  :tags: 框架, electron
  :category: 前端
  :author: YanQue
  :location: CD
  :language: zh-cn


在 `package.json` 的 `build` 位置::

  "build": {                    // electron-builder的配置
    "productName":"xxxx",       // 项目名 这也是生成的exe文件的前缀名
    "appId": "com.xxx.xxxxx",   // 包名
    "copyright":"xxxx",         // 版权  信息
    "directories": {
      "output": "build"         // 输出文件夹, 只能配置输出的上面几层,
                                // 比如mac下默认输出位置是 dist/mac,
                                // 在这里配置了output 为 dist/myapp,
                                // 最终输出位置还是有mac, 会变成 dist/myapp/mac
                                // 坑的一批
    },

    // windows相关的配置
    "win": {
      "icon": "xxx/icon.ico"// 图标路径
    }
  }

部分参考: https://segmentfault.com/a/1190000017296201



