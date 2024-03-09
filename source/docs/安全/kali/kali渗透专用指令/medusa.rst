=======================
medusa
=======================

暴力破解帐密

示例
=======================

.. code-block:: sh

	# password存放在pwd.txt
	# 以ssh形式破解192.168.135.123帐密
	medusa -M ssh -h 192.168.135.123 -u root -P pwd.txt

