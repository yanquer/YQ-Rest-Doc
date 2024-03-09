====================================
lxml
====================================

- github地址: `<https://github.com/lxml/lxml>`_
- 官方主页: `<https://lxml.de>`

需要先了解 :doc:`/docs/后端/python/教程/xpath/index` 的前置知识

安装::

  pip install lxml


lxml提供了两种解析网页的方式，一种是你解析自己写的离线网页时，另一种 则是解析线上网页。

导入包::

  from lxml import  etree

1.解析离线网页::

  html=etree.parse('xx.html',etree.HTMLParser())
  aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
  print(aa)

2.解析在线网页::

  from lxml import etree
  import requests
  rep=requests.get('https://www.baidu.com')
  html=etree.HTML(rep.text)
  aa=html.xpath('//*[@id="s_xmancard_news"]/div/div[2]/div/div[1]/h2/a[1]/@href')
  print(aa)

