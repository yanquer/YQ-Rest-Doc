=============
requests
=============


.. post:: 2023-02-20 22:06:49
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn



下载文件
=============

小文件
-------------

小文件::

  import requests

  url = "http://www.test.com/xxxxx/test.jpg"
  path = r"c:\test.jpg"

  req = requests.get(url)
  with open(path, "wb") as f:
      f.write(req.content)


大文件
-------------

断点续传::

  import sys
  import requests
  import os


  class Downloader(object):
      def __init__(self, url, file_path):
          self.url = url
          self.file_path = file_path

      def start(self):
          res_length = requests.get(self.url, stream=True)
          total_size = int(res_length.headers['Content-Length'])
          print(res_length.headers)
          print(res_length)
          if os.path.exists(self.file_path):
              temp_size = os.path.getsize(self.file_path)
              print("当前：%d 字节， 总：%d 字节， 已下载：%2.2f%% " % (temp_size, total_size, 100 * temp_size / total_size))
          else:
              temp_size = 0
              print("总：%d 字节，开始下载..." % (total_size,))

          headers = {'Range': 'bytes=%d-' % temp_size,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
          res_left = requests.get(self.url, stream=True, headers=headers)

          with open(self.file_path, "ab") as f:
              for chunk in res_left.iter_content(chunk_size=1024):
                  temp_size += len(chunk)
                  f.write(chunk)
                  f.flush()

                  done = int(50 * temp_size / total_size)
                  sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                  sys.stdout.flush()


  if __name__ == '__main__':
      url = "http://www.test.com/xxxxx/test.jpg"
      path = r"c:\test.jpg"
      downloader = Downloader(url, path)
      downloader.start()

.. note::

  若文件下载 url 存在重定向, 则使用 ``allow_redirects=True`` ::

    requests.get(url, allow_redirects=True)

  分块下载使用 ``stream=True`` ::

    requests.get(url, stream=True)

  断点续传需要指定 headers 下的 Range 字段 来指定范围 ::

    # 或者 headers = {'Range': 'bytes=%d-'%(start,)}
    headers = {'Range': 'bytes=%d-%d'%(start,end)}

关于文件下载时候的路径
==========================

当从一个url下载文件时候, 若使用绝对路径, 不会有问题.

但可能有时候不想使用绝对路径, 而是使用相对路径, 那么这个时候可能就会
存在给定的下载路径正确, 但就是说路径不存在, 下载不了, 也没发使用python执行(若是可执行文件).

这个时候可能是文件名的命名使用了url编码的缘故,
而其中可能有些特殊字符不能被python正常解析, 故而导致的这个问题
将名称使用url解码即可::

  urllib.parse.unquote(url_path)


