===========================
grpc使用入门
===========================


.. post:: 2024-03-09 18:21:01
  :tags: python, python三方库
  :category: 后端
  :author: YanQue
  :location: CD
  :language: zh-cn



RPC, 远程过程调用服务, 注重传输协议于序列化.

一些认识 :doc:`/docs/杂乱无章/计算机网络/HTTP认识`

gRPC是由Google公司开源的高性能RPC框架。支持多语言、多平台，
其消息协议使用Google自家开源的Protocol Buffers协议机制（proto3） 序列化，传输使用HTTP/2标准，支持双向流和连接多路复用。

安装
===========================

安装::

    pip install grpc grpcio-tools

使用流程(用例说明)
===========================

以一个用例说明.

背景: 业务已有一个 Cat 类, 如下

.. literalinclude:: ../../../../../.test/test_rpc_cat/cat.py
    :caption: Cat类
    :language: python

需要与之相关的 rpc 服务来获取其属性

流程:

- 编写proto文件, 定义数据通信协议
- 根据编写好的proto协议文件, 生成相应的python文件
- 编写server服务端
- 编写client客户端


编写 proto 协议文件
---------------------------

根据需求编写好proto协议文件如下:

.. literalinclude:: ../../../../../.test/test_rpc_cat/rpc_cat.proto
    :caption: cat协议文件
    :language: protobuf

其中, 使用message来自定义消息类型, 如定义一个String消息, 只包含一个string类型数据::

    message StringMessage{
        string message = 1;
    }

.. tip::

    可用 map 定义map类型

    可用 repeated 来表示可重复类型, 如::

        repeated string message = 1;

    注意map默认可重复, 不能加 repeated.

私以为, 一般情况下, 对于普通的数据或者约定好的通用接口类型返回, 使用message定义较方便,
但是对于其中的复杂数据类型, 还是使用 bytes 传递二进制数据, 获取后自行处理较方便.

记得大学学java的那段时间, 接口一般都是使用 Result 封装的, 大概如下::

    class Result(){
        int code;
        string message;
        Map<T, T> data;
    }

应该是这样, 具体记不清了, 很久没用了.

如果将这么一个约定好的接口返回写进proto, 那么可以这样::

    message Result{
        int32 code = 1;
        string message = 2;
        bytes data = 3;
    }

.. sidebar::

    这里message定义消息属性的值为 1, 2, 3 , 并非强制这样写, 我看网上大多都是按照123顺序定义值, 多半是跟着官网文档用例来的.

    另外本文的协议文件定义了较多数据类型, 正式使用时是不建议的, 最好是只定义一个请求类型, 一个返回类型吧, 此处为用例只是表示可以这么写.

可以看出对于基本的数据类型, 可以很方便定义, 哪怕是复杂一点, 比如有一个 Person 类, 也可以进行多层封装.

但是对于python而言, 尤其是字典类型, 其值的类型大多都不是指定的, 比如本例的 Cat 类获取所有属性(get_all)::

    def all_attr(self):
        return {
            'name': self._name, 	# 这是 str
            'age':  self._age,		# 这是 int
            'love': self._love,		# 这是 tuple
            'food_once': self._eat_food_once,	# 这个则是 Dict[str, float]
        }

这个时候使用 message 中的普通类型封装就很难, 所以还是决定使用 bytes 直接传递二进制的data数据方便些.

RpcCat 是rpc服务, 内定义了将支持哪些调用, 如::

    rpc get_name (EmptyMessage) returns (StringMessage) {}

表示定义一个rpc调用, 名为 get_name, 请求参数类型为 EmptyMessage,
返回参数类型为 StringMessage (两类型已用message定义).

生成相应的python文件
---------------------------

根据编写好的proto文件生成对应的py文件::

    mkdir proto
    python -m grpc_tools.protoc --pyi_out=./proto --python_out=./proto --grpc_python_out=./proto -I. rpc_cat.proto

参数解释:

-IPATH, --proto_path=PATH	proto文件路径, 包括导入的
--pyi_out=OUT_DIR			Generate Python pyi stub.
--python_out=OUT_DIR		Generate Python source file.
--grpc_python_out=OUT_DIR	Generate Python source file.

注意这里我放到了 proto 文件夹下, 需要自行处理一下环境导入问题::

    cd proto

    echo "import sys
    sys.path.append('./proto')
    " > __init__.py

.. note::

    protoc: protobuf 编译器(compile), 将 proto 文件编译成不同语言的实现, 这样不同语言中的数据就可以和 protobuf 格式的数据进行交互

    protobuf 运行时(runtime): protobuf 运行时所需要的库, 和 protoc 编译生成的代码进行交互

编写server服务端
---------------------------

源码:

.. literalinclude:: ../../../../../.test/test_rpc_cat/rpc_server.py
    :caption: server端
    :language: python

注意传参必须使用位置参数::

    # message=self._cat.love() 的 message不能丢
    return rpc_cat_pb2.TupleMessage(message=self._cat.love())

否则会有报错::

    TypeError: No positional arguments allowed

编写client客户端
---------------------------

源码:

.. literalinclude:: ../../../../../.test/test_rpc_cat/rpc_client.py
    :caption: client端
    :language: python

.. sidebar::

    字典数据直接使用 bytes 定义消息, 使用 json 转换, 较好.

.. note::

    python 可用的 rpc 框架还是比较多的, 比如 grpc, thrift, rryc等

    其中 grpc 等拓展性稳定性是最好的

    thrift 对 python 的支持不是很好, 但是支持多语言

    rryc 基本是服务于纯python, 对只使用 python 的服务较友好


支持的通信方式
===========================

- 一次请求, 一次应答
- 一次请求, 流式应答
- 流式请求, 一次应答
- 流式请求, 流式应答

如要使用流式请求/应答, 参数类型前加 **stream** 即可. 比如上面的例子, 定义了 流请求, 应答流::

    rpc get_attr_by_name_with_stream (stream StringMessage) returns (stream StringMessage) {}

对于python代码中的实现, 使用迭代器就好.

client端, 请求::

    @property
    def _connection(self):
        if self._stub is None:
            # with grpc.aio.insecure_channel('localhost:50052') as channel:
            self._stub = cat_pb2_grpc.RpcCatStub(grpc.aio.insecure_channel('localhost:50052'))
        return self._stub

    def get_attr_by_stream(self):

        def stream_message():
            for s in ('name', 'age', 'love'):
                yield cat_pb2.StringMessage(message=s)

        response = self._connection.get_attr_by_name_with_stream(stream_message())

        return [x for x in response]

server端, 应答::

    def get_attr_by_name_with_stream(self, request_iterator, context):
        for request in request_iterator:
            yield rpc_cat_pb2.StringMessage(message=self._cat.get_attr_by_name(request.message))


