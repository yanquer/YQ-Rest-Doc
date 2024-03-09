===================================
使用diff编辑器打开两个文件对比
===================================

首先, 要有两个URI路径
(theia封装的URI: ``import URI from '@theia/core/lib/common/uri'``)::

  import URI from '@theia/core/lib/common/uri'

  const leftUri = new URI('file:///c:/users/bob.txt')
  const rightUri = new URI('file:///c:/users/bob2.txt')

然后使用DiffUris封装这两个URI::

  import {DiffUris} from '@theia/core/lib/browser/diff-uris'

  const diffU: URI = DiffUris.encode(leftUri, rightUri)

然后在使用open打开::

  import {OpenerService, open} from '@theia/core/lib/browser'

  @inject(OpenerService) readonly _openerService: OpenerService

  open(this._openerService, diffU)






