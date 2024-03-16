============================
记录vs下载安装慢的问题
============================


.. post:: 2023-06-11 18:06:14
  :tags: 
  :category: 杂乱无章
  :author: YanQue
  :location: CD
  :language: zh-cn



- 首先获取下载地址,  比如下载vs2022相关软件包,  地址就是 `download.visualstudio.microsoft.com` (得自己找)
- 去 `DNS查询网站 <https://tool.chinaz.com/dns>`_ 查询相关改下载地址的相关信息, 然后选择 ttl 最小的那个, 设置DNS

	.. figure:: ../../resources/images/2022-12-11-17-04-04.png
		:align: center
		:width: 480px

		dns网站查询

- 最后去windows修改DNS配置 (效果不一定)

	.. figure:: ../../resources/images/2022-12-11-17-07-28.png
		:align: center
		:width: 480px

		修改dns配置


.. note::

	顺便说一句,  想起之前windows登录微软账号时,  一直链不上网,  后面取消 ipv6 就可以了。

