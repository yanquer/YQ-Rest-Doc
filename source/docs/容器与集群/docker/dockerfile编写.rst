==============================
dockerfile编写
==============================


.. post:: 2023-02-20 22:06:49
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


定制docker镜像的方式有两种

- 手动修改容器内容，导出新的镜像;
  相关指令:

  - docker commit 将容器提交为镜像
- 基于Dockerfile自行编写指令，基于指令流程创建镜像

.. note::

  前置知识: 镜像是分层的; 容器以镜像为基础层, 本身为运行时存储层

关键字
==============================

每一句关键字指令都会生成一个镜像层

FROM
  **必须**, 基于的基础镜像, 比如 debian, 没有基础镜像, 没法运行上面的层
RUN
  执行什么指令, 比如::

    apt install xxx
VOLUME
  设置卷，挂载主机目录; 如建立的数据目录,
  比如::

    # 将 /var/lib/xxx 设置为挂载卷(mount)
    VOLUME /var/lib/xxx

    # 将容器内的 /var/lib/xxx 文件夹，在容器运行时，
    # 该目录自动挂载为匿名卷，任何向该目录中写入数据的操作，
    # 都不会被容器记录，保证的容器存储层无状态理念

  如果有多个::

    VOLUME ["/var/lib/xxx", "/var/lib/xxx2", "/var/lib/xxx3", ...]

  容器在运行时，应该保证在存储层不写入任何数据，运行在容器内产生的数据，
  推荐是 **挂载，写入到宿主机上，进行维护。**

  如果run的时候没有-v手动指定挂载, 指定的内容会自动挂载到宿主机, 可以使用::

    docker inspect $container_name

  检查挂载的位置
MAINTAINER
  指定维护者信息，可以没有
ADD
  COPY宿主机的文件到容器内, 会自动解压

  还支持 URL 下载链接, 权限默认600, 但是这时不会解压(如果是压缩包)

  官方更推荐COPY, 因为ADD包含了更多复杂的功能，且ADD会使构建缓存失效，导致镜像构建缓慢
WORKDIR
  设置当前工作目录
USER
  设置当前用户
EXPOSE
  指定容器运行时对外提供的端口服务，

  - 帮助使用该镜像的人，快速理解该容器的一个端口业务

  相关指令::

    docker port 容器  # 查看已经映射的端口
    docker run -p 宿主机端口：容器端口
    docker run -P     # 作用是随机宿主机端口：容器内端口
CMD
  指定容器启动后的要干的事情,
  语法::

    CMD ["参数1", "参数2"]

  与直接在docker run 最后写command效果一致.
  即该镜像在运行容器实例的时候，执行的具体参数是什么,
  如::

    docker run -it debian bash  # 注意这里的优先级高于CMD的, 也就是如果指定了会覆盖CMD的 定义
    # 就相当于dockerfile的
    CMD ["bash"]

  貌似很多默认行为就是::

    CMD ["/bin/bash"]

  如果是多个要分开::

    CMD ["cat", "/etc/debian_version"]

  如果指定了 ENTRYPOINT, CMD指定具体的参数就是传给 ENTRYPOINT
ENV
  设置环境变量;
  比如::

    ENV a 1
COPY
  COPY宿主机的文件到容器内, 不会自动解压
ENTRYPOINT
  容器启动后执行的命令. 作用和CMD一样

  当指定了 ENTRYPOINT, CMD指定具体的参数就是传给 ENTRYPOINT
ARG
  设置环境变量, 这点与ENV一致;
  区别在于:

  - ENV 无论是在镜像构建时，还是容器运行，该变量都可以使用;
  - ARG只是用于构建镜像需要设置的变量，容器运行时就消失了

创建
==============================

.. note::

  创建的文件名必须时 Dockerfile / dockerfile

写好后构建出镜像::

  docker build .

经典问题::

  CMD systemctl start nginx

  这样的写法是错误的，容器会立即退出

  因为systemct1 start nginx是希望以守护进程形式启动nginx，且CMD命令会转化为

  CMD ["sh"，"-C"， "systemctl start nginx"]

  这样的命令主进程是sh解释器，执行完毕后立即结束了，因此容器也就退出了。

  因此正确的做法应该是CMD ["nginx"，"-g"，"daemon off；"]



