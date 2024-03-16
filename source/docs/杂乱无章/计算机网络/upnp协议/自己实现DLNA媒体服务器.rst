=================================
自己实现DLNA媒体服务器
=================================


.. post:: 2024-03-09 18:21:01
  :tags: upnp协议
  :category: 计算机网络
  :author: YanQue
  :location: CD
  :language: zh-cn


实现一个完备的媒体服务器, 需要的设备服务分类
==========================================================

MediaServer设备: 提供资源发现和访问

- **必选服务:MediaServer**, 媒体服务器服务, 提供媒体资源发现和元数据访问

  - 公开服务器上的媒体资源,客户端可以浏览和搜索资源
  - 客户端选择资源后,获取资源的详细信息(元数据)和流URL
- **必选服务:ContentDirectory**, 内容目录服务
  - 将存储在UPnP媒体服务器上的资源以树形结构组织起来方便浏览
  - 支持根据资源类型(容器、对象)或元数据属性对资源进行过滤和搜索
  - 允许控制点检索存储在服务中的资源的详细信息
- 可选服务:ConnectionManager, 连接管理器服务, 管理对服务器的连接,验证和授权客户端。可选服务.
  若提供敏感数据或服务,需要对访问进行控制, 推荐实现

MediaRenderer设备: 获取流播放

- **必选服务:MediaRenderer,AVTransport**
- 可选服务:ConnectionManager,MediaServer

其中:

- 媒体渲染器服务(MediaRenderer):获取和解码播放流媒体

  - 接收客户端指定的流URL,从URL中获取媒体流
  - 解码并播放收到的媒体流,实现远程流媒体播放
- AV传输服务(AVTransport):控制MediaRenderer的播放

  - 用于控制MediaRenderer的播放,实现播放控制(播放/暂停/停止/Seek等)
  - 发布播放状态和进度等,供客户端监控
- 连接管理器服务(ConnectionManager):管理对渲染器的连接,可选服务

  - 用于管理客户端与媒体服务器/渲染器的连接
  - 验证客户端,授权流连接,并在连接断开时清理资源
  - 提供流媒体播放服务, 若需要对连接和 Play 进行控制, 则推荐实现
- 媒体服务器服务(MediaServer):可选服务,如果MediaRenderer也存储资源可以实现。

**如果一个设备同时具备资源存储+流媒体播放的功能,也可以选择只实现MediaRenderer设备,
并在其中同时包含MediaServer与MediaRenderer服务。但这需要MediaRenderer标准能够满足对应要求**

具体可以通过以下设备描述将其定义为一个MediaServer+MediaRenderer设备::

  <root xmlns="urn:schemas-upnp-org:device-1-0">
  <specVersion>
  <major>1</major>
  <minor>0</minor>
  </specVersion>
  <device>
  <deviceType>urn:schemas-upnp-org:device:MediaServer:1</deviceType>
  <friendlyName>MY MEDIA SERVER</friendlyName>
  ...
  </device>
  <device>
  <deviceType>urn:schemas-upnp-org:device:MediaRenderer:1</deviceType>
  <friendlyName>MY MEDIA RENDERER</friendlyName>
  ...
  </device>
  </root>

该描述, 定义了一个带MediaServer和MediaRenderer设备类型的UPnP设备。从而在一个物理设备上提供完整的远程媒体浏览、播放和控制功能。

最小化存储媒体服务器
==========================================================

仅实现一个具有存储功能的设备服务, 类似于纯文件服务器, 媒体播放方面如解码/编码等由客户端自己实现.

可行方案:

使用设备:

MediaServer
  - ContentDirectory:提供文件存储目录和文件元数据的访问
  - ConnectionManager:管理客户端连接

这时候客户端需要实现

- MediaRenderer:获取文件数据,解码并播放
- AVTransport:自己实现播放控制
- ConnectionManager:管理连接服务器获取文件

工作流程为:

1. 客户端通过ContentDirectory浏览文件服务器上的文件,获取文件元数据
2. 客户端选择文件后,通过ConnectionManager与文件服务器建立连接,获取文件数据
3. 客户端自身具备解码和播放文件的能力,使用自己的MediaRenderer和AVTransport实现文件播放
4. 客户端可以控制自己的播放,无需依赖服务器

这种方案的优点是:

1. 文件服务器实现简单,只需提供文件存储和访问
2. 客户端有更大的灵活性,可以选择任意的解码和播放方案
3. 兼容性好,任何能够获取文件并播放的客户端都可以访问

缺点是:

1. 客户端需要自行实现较复杂的流媒体播放功能
2. 播放体验依赖客户端,无法统一
3. 无法利用UPnP等标准来简化开发和提高互操作性

如果文件服务器只提供文件存储功能,依赖客户端实现播放,这种方案是可行的,可以获得较好的兼容性和灵活性。
但客户端开发会较为复杂,无法利用UPnP等标准来简化流程。

如果想进一步利用UPnP标准,可以考虑文件服务器实现:
设备类型:MediaServer+MediaRenderer
对应服务:
- ContentDirectory
- ConnectionManager
- MediaRenderer
- AVTransport

这样文件服务器可以直接对获取的文件解码和播放,并使用标准的AVTransport实现播放控制,这可以最大限度简化客户端开发,利用UPnP标准提高互操作性。同时也控制了播放体验,这是一种更佳的实现方案。

但是这样客户端只能进行项目浏览(看有哪些文件/文件夹), 不能访问具体的媒体数据(不能媒体传输播放视频).

若需要支持数据传输, 还需要实现:

- MediaRenderer 服务, 使用下面的 GetMediaInfo action来获取媒体数据.

GetMediaInfo Action的输入输出参数如下:

输入参数:

- InstanceID: 媒体实例ID,由Browse等Action返回
- Filter: 指定返回的数据类型,如:”*”返回所有信息

输出参数:

- CurrentSrc: 媒体URL,指向实际的媒体文件
- MetaInfo: 媒体元数据信息
- Data: 实际的媒体文件数据,二进制

对应的参数类型为:

- InstanceID: string
- Filter: string
- CurrentSrc: string,url
- MetaInfo: string,xml
- Data: bin.base64

典型的调用流程为:

1. 客户端调用ContentDirectory的BrowseAction获取要播放的媒体InstanceID
2. 使用InstanceID调用GetMediaInfo Action,同时指定Filter为"*",表示返回所有信息
3. 服务器返回CurrentSrc(媒体URL)、MetaInfo(元数据)和Data(文件数据)
4. 客户端获取Data,调用系统API进行解码和播放
5. 客户端可以使用Seek, Pause等Action控制播放

当客户端要主动获取服务器上的媒体文件并自行播放时,GetMediaInfo这个Action是最关键的。
它可以返回媒体的URL,元数据和文件数据,让客户端获得全部所需信息进行播放。



