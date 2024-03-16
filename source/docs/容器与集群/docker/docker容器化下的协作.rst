====================================
docker容器化下的协作开发
====================================


.. post:: 2023-02-20 22:06:49
  :tags: docker
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


**持续交付部署**

保障一致性的环境

开发人员
  代码写好之后，还会开发 dockerfile 脚本完成，
  将代码，和环境依赖，全部打包为一个镜像文件(images)
测试
  直接拿 images, docker run
运维
  直接拿 images, docker run



