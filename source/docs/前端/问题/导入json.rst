=============================
导入json
=============================

对于ts项目而言

在 `tsconfig.json` 增加以下内容::

  {
    "compilerOptions": {
      "resolveJsonModule": true
    }
  }

然后直接::

  import * as schemeData from 'xxxxx.json'

即可





