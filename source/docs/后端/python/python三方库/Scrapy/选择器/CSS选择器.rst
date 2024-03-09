================================
CSS选择器
================================

主要是用法.

概述::

  ::text            获取文本
  ::attr(属性名)    获取指定属性
  *::text           * 表示所有, 即获取所有文本

比如有::

  如有以下HTML::

  <!DOCTYPE html>

  <html>
    <head>
      <base href='http://example.com/' />
      <title>Example website</title>
    </head>
    <body>
      <div id='images'>
        <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
        <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
        <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
        <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
        <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
      </div>
    </body>
  </html>

选择title的内容::

  title::text

获取 href::

  html head base::attr(className)

获取所有 image 下的文本::

  #images *::text

在代码中就是::

  >>> response.css("#images *::text").getall()
  ['\n   ',
  'Name: My image 1 ',
  '\n   ',
  'Name: My image 2 ',
  '\n   ',
  'Name: My image 3 ',
  '\n   ',
  'Name: My image 4 ',
  '\n   ',
  'Name: My image 5 ',
  '\n  ']




