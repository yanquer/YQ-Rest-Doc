==============================
Chrome搜索技巧
==============================


.. post:: 2024-03-09 18:21:01
  :tags: Chrome
  :category: 常用工具使用
  :author: YanQue
  :location: CD
  :language: zh-cn


site
==============================

指定搜索时(不)查询某个域名(比如csdn)::

  今日大瓜 -site:csdn.net

说明:

- 无空格是不搜索指定域名 ``-site:csdn.net``
- 有空格是仅搜索指定域名 ``-site: csdn.net``
- 无 ``-`` 时, 不管有无空格, 都是仅搜索指定域名 ``site: csdn.net``, ``site:csdn.net``

intitle
==============================

网页 **标题** 必须包含的内容::

  intitle:今日大瓜

intext
==============================

网页 **内容** (正文)必须包含的内容::

  intext:今日大瓜

inurl
==============================

地址必包含的url, 如::

  inurl:index.php?id=

filetype
==============================

文件类型::

  filetype:pdf




