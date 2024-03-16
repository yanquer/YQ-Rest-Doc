=================================
SelectorList
=================================


.. post:: 2023-03-01 22:50:22
  :tags: python, python三方库, Scrapy, API
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn


:doc:`/docs/后端/python/python三方库/Scrapy/API/Selector`
有的对象方法, 好像它也有.


对象方法

get(default=""): str | None
  获取第一个元素的data
getall(): [str]
  获取所有查询到的列表selector的data
re(args)
  对数据集的data, 进行正则查询
attrib["src"]
  不使用 :doc:`/docs/后端/python/python三方库/Scrapy/选择器/index` 获取属性

  而是直接使用实例方法获取属性::

    response.css("img").attrib["src"]
    # 即 img::attr(src)
    # 或 //img/@src
extract_first()
  与 get 一致, 主要是为了兼容其他的(其他框架有这个), 下同
extract()
  与 getall 一致

