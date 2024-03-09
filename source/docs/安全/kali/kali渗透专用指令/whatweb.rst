======================
whatweb
======================

用于CMS指纹识别   
.. 服务框架扫描, VUE啥的.

示例
======================

.. code-block:: sh

	┌──(yanque㉿kali)-[~]
	└─$ whatweb -v www.baidu.com
	WhatWeb report for http://www.baidu.com
	Status    : 200 OK
	Title     : 百度一下，你就知道
	IP        : 14.215.177.38
	Country   : CHINA, CN

	Summary   : Cookies[BAIDUID,BDSVRTM,BD_HOME,BIDUPSID,H_PS_PSSID,PSTM], Email[index@2.png,pop_tri@1x-f4a02fac82.png,qrcode-hover@2x-f9b106a848.png,qrcode@2x-daf987ad02.png,result@2.png], HTML5, HTTPServer[BWS/1.1], JQuery, Meta-Refresh-Redirect[http://www.baidu.com/baidu.html?from=noscript], OpenSearch[/content-search.xml], Script[application/json,text/javascript], UncommonHeaders[bdpagetype,bdqid,traceid], X-Frame-Options[sameorigin], X-UA-Compatible[IE=Edge,chrome=1,IE=edge]

	Detected Plugins:
	[ Cookies ]
		Display the names of cookies in the HTTP headers. The
		values are not returned to save on space.

		String       : BAIDUID
		String       : BIDUPSID
		String       : PSTM
		String       : BAIDUID
		String       : BDSVRTM
		String       : BD_HOME
		String       : H_PS_PSSID

	[ Email ]
		...
		...

	HTTP Headers:
		HTTP/1.1 200 OK
		Accept-Ranges: bytes
		Cache-Control: max-age=86400
		Content-Encoding: gzip
		Content-Length: 1131
		Content-Type: text/html
		Date: Mon, 02 Jan 2023 10:15:00 GMT
		Etag: "b83-59bafefa98680"
		Expires: Tue, 03 Jan 2023 10:15:00 GMT
		Last-Modified: Thu, 09 Jan 2020 07:27:06 GMT
		P3p: CP=" OTI DSP COR IVA OUR IND COM "
		Server: Apache
		Set-Cookie: BAIDUID=D4BF2F2CC2550CD470A3E182B2D10463:FG=1; expires=Tue, 02-Jan-24 10:15:00 GMT; max-age=31536000; path=/; domain=.baidu.com; version=1
		Vary: Accept-Encoding,User-Agent
		Connection: close

	┌──(yanque㉿kali)-[~]
	└─$


