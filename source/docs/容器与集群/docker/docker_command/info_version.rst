======================
info|version
======================


.. post:: 2023-02-20 22:06:49
  :tags: docker, docker_command
  :category: 容器与集群
  :author: YanQue
  :location: CD
  :language: zh-cn


info
-----------------------

| 显示 Docker 系统信息，包括镜像和容器数

语法
+++++++++++++++++++++++

``docker info [OPTIONS]``

示例
+++++++++++++++++++++++

查看docker系统信息

.. code-block:: sh

	yanque@yanquedembp ~ % docker info
	Client:
	Context:    default
	Debug Mode: false
	Plugins:
	buildx: Docker Buildx (Docker Inc., v0.9.1)
	compose: Docker Compose (Docker Inc., v2.13.0)
	dev: Docker Dev Environments (Docker Inc., v0.0.5)
	extension: Manages Docker extensions (Docker Inc., v0.2.16)
	sbom: View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
	scan: Docker Scan (Docker Inc., v0.22.0)

	Server:
	Containers: 1
	Running: 0
	Paused: 0
	Stopped: 1
	Images: 3
	Server Version: 20.10.21
	Storage Driver: overlay2
	Backing Filesystem: extfs
	Supports d_type: true
	Native Overlay Diff: true
	userxattr: false
	Logging Driver: json-file
	Cgroup Driver: cgroupfs
	Cgroup Version: 2
	Plugins:
	Volume: local
	Network: bridge host ipvlan macvlan null overlay
	Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
	Swarm: inactive
	Runtimes: runc io.containerd.runc.v2 io.containerd.runtime.v1.linux
	Default Runtime: runc
	Init Binary: docker-init
	containerd version: 770bd0108c32f3fb5c73ae1264f7e503fe7b2661
	runc version: v1.1.4-0-g5fd4c4d
	init version: de40ad0
	Security Options:
	seccomp
	Profile: default
	cgroupns
	Kernel Version: 5.15.49-linuxkit
	Operating System: Docker Desktop
	OSType: linux
	Architecture: x86_64
	CPUs: 4
	Total Memory: 7.675GiB
	Name: docker-desktop
	ID: OY2O:RZL6:WSMC:6CSU:F2F4:ETDE:JYMM:UYOJ:O3DU:VMV5:NPFN:PA3X
	Docker Root Dir: /var/lib/docker
	Debug Mode: false
	HTTP Proxy: http.docker.internal:3128
	HTTPS Proxy: http.docker.internal:3128
	No Proxy: hubproxy.docker.internal
	Registry: https://index.docker.io/v1/
	Labels:
	Experimental: false
	Insecure Registries:
	hubproxy.docker.internal:5000
	127.0.0.0/8
	Registry Mirrors:
	https://0b27f0a81a00f3560fbdc00ddd2f99e0.mirror.swr.myhuaweicloud.com/
	https://ypzju6vq.mirror.aliyuncs.com/
	https://registry.docker-cn.com/
	http://hub-mirror.c.163.com/
	https://docker.mirrors.ustc.edu.cn/
	Live Restore Enabled: false

	yanque@yanquedembp ~ %


version
-----------------------

| 显示 Docker 版本信息。

语法
+++++++++++++++++++++++

``docker version [OPTIONS]``

.. topic:: OPTIONS说明：

	- -f :指定返回值的模板文件。

示例
+++++++++++++++++++++++

显示 Docker 版本信息

.. code-block:: sh

	yanque@yanquedembp ~ % docker version
	Client:
	Cloud integration: v1.0.29
	Version:           20.10.21
	API version:       1.41
	Go version:        go1.18.7
	Git commit:        baeda1f
	Built:             Tue Oct 25 18:01:18 2022
	OS/Arch:           darwin/amd64
	Context:           default
	Experimental:      true

	Server: Docker Desktop 4.15.0 (93002)
	Engine:
	Version:          20.10.21
	API version:      1.41 (minimum version 1.12)
	Go version:       go1.18.7
	Git commit:       3056208
	Built:            Tue Oct 25 18:00:19 2022
	OS/Arch:          linux/amd64
	Experimental:     false
	containerd:
	Version:          1.6.10
	GitCommit:        770bd0108c32f3fb5c73ae1264f7e503fe7b2661
	runc:
	Version:          1.1.4
	GitCommit:        v1.1.4-0-g5fd4c4d
	docker-init:
	Version:          0.19.0
	GitCommit:        de40ad0
	yanque@yanquedembp ~ %


