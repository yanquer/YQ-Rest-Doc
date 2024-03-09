=======================
docker常用指令
=======================

.. 常用命令-Docker
.. =======================

.. toctree::
  :maxdepth: 1

  docker_command/index


其它
-----------------------


.. code-block:: sh
  :caption: Docker 常用命令

  # 登录私有地址, 可加 --username= 指定用户名, 然后手动输入密码
  docker login $address
  # cat ~/.docker/config.json 验证是否成功, 成功登录有 auths 配置

  # 拉取镜像, 公共仓库用镜像名字, 私有仓库用地址名加镜像名字
  docker pull $image_name

  # 上传镜像, 公共仓库不用地址直接镜像名即可
  docker push $address $image_name

  # 查看已下载镜像
  docker images

  # 运行一个容器, 若不存在自动从官网拉取
  # -d 后台运行
  # -p 后跟端口 port1:port2 将容器内部服务器端口port2映射到本地端口port1(如果-p后什么也不写，随机分配端口)
  # --rm 容器停止之后会自动删除
  docker run $image_name

  # 搜索镜像
  docker search $image_name

  # 查看所有容器
  # ps 查看运行中的docker
  docker ps -a

  # 删除容器
  docker rm 容器id

  # 启动容器
  docker start 容器id

  # 停止所有容器
  docker stop $(docker ps -a -q)

  # remove删除所有容器
  docker rm $(docker ps -a -q)

  # 重启容器
  docker restart $image_name

  # 查看日志, 如查看mysql日志
  docker logs -f mysql57

  # 进入容器, 如进入mysql容器
  # -t 在容器里生产一个伪终端
  # -i 对容器内的标准输入 (STDIN) 进行交互
  docker exec -ti mysql57 /bin/bash

  # 查看容器信息
  docker inspect $image_name

.. code-block:: sh
  :caption: docker run 参数

  # 例子
  docker run -p 3306:3306 --name mysql57 \
  -v $PWD/conf:/etc/mysql \
  -v $PWD/logs:/var/log/mysql \
  -v $PWD/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -d mysql:5.7 \
  --character-set-server=utf8mb4 \
  --collation-server=utf8mb4_unicode_ci

  # 参数选项
  –name：容器名, 比如mysql57
  -v：挂载目录
  -e：配置信息, 比如配置mysql的root用户的登陆密码
  -p：端口映射, 比如映射 主机3306端口 到 容器的3306端口
  -d：源镜像名, 比如为 mysql:5.7并后台运行 后面为设置mysql的默认编码

