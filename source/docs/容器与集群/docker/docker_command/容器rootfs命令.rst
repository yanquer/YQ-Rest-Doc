========================
容器rootfs命令
========================

commit
-----------------------

| 从容器创建一个新的镜像

语法
+++++++++++++++++++++++

``docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]``

.. topic:: OPTIONS说明：

	- -a :提交的镜像作者；
	- -c :使用Dockerfile指令来创建镜像；
	- -m :提交时的说明文字；
	- -p :在commit时，将容器暂停。

示例
+++++++++++++++++++++++

将容器 ea0a6afe23a3 保存为新的镜像, 设置仓库名为 `kali`, tag为 `config_apt_list2` , 并添加提交人信息和说明信息。

.. code-block:: sh

	(dev_venv) yanque@yanquedeMacBook-Pro project % docker commit -a 'yanque' -m 'kali image with config ustc apt list' ea0a6afe23a3 kali:config_apt_list2
	sha256:24b7cbbe11fb587bf850dad2f2dc1b46412a2c73c2b55a00716dabb1b7832204
	(dev_venv) yanque@yanquedeMacBook-Pro project %
	(dev_venv) yanque@yanquedeMacBook-Pro project % docker images kali:config_apt_list2
	REPOSITORY   TAG                IMAGE ID       CREATED          SIZE
	kali         config_apt_list2   24b7cbbe11fb   56 seconds ago   236MB

cp
-----------------------

| docker cp :用于容器与主机之间的数据拷贝。

语法
+++++++++++++++++++++++

- ``docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-``

- ``docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH``

.. topic:: OPTIONS说明：

	- -L :保持源目标中的链接

示例
+++++++++++++++++++++++

将主机 *README.en.md* 拷贝到容器 *mykali* 的 */root* 目录下。

.. code-block:: sh
	:emphasize-lines: 1

	yanque@yanquedembp mytest % docker cp README.en.md mykali:/root
	yanque@yanquedembp mytest % ls -lh README.en.md
	-rw-r--r--  1 yanque  staff   816B 10 22 02:12 README.en.md
	yanque@yanquedembp mytest %
	yanque@yanquedembp mytest % docker exec -it mykali /bin/bash
	┌──(root㉿fa15654fc7d1)-[/]
	└─#
	┌──(root㉿fa15654fc7d1)-[~]
	└─# cd ~ && ls -lh
	total 4.0K
	-rw-r--r-- 1 501 dialout 816 Oct 21 18:12 README.en.md

	┌──(root㉿fa15654fc7d1)-[~]
	└─#

diff
-----------------------

| docker diff : 检查容器里文件结构的更改

语法
+++++++++++++++++++++++

``docker diff [OPTIONS] CONTAINER``

示例
+++++++++++++++++++++++

查看容器 *mykali* 的文件结构更改。

.. code-block:: sh

	yanque@yanquedembp ~ % docker diff mykali
	C /root
	C /root/.bash_history
	yanque@yanquedembp ~ %

