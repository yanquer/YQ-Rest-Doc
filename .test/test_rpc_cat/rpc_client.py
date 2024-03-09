# coding: utf-8
import asyncio
import json
import logging

import grpc

import proto.rpc_cat_pb2 as cat_pb2
import proto.rpc_cat_pb2_grpc as cat_pb2_grpc


class RpcClient(object):

    _stub = None

    @property
    def _connection(self):
        if self._stub is None:
            # with grpc.aio.insecure_channel('localhost:50052') as channel:
            self._stub = cat_pb2_grpc.RpcCatStub(grpc.aio.insecure_channel('localhost:50052'))
        return self._stub

    def get_name(self):
        return self._connection.get_name(cat_pb2.EmptyMessage())

    def get_age(self):
        return self._connection.get_age(cat_pb2.EmptyMessage())

    def get_food(self):
        return self._connection.get_food_once(cat_pb2.EmptyMessage())

    def get_love(self):
        return self._connection.get_love(cat_pb2.EmptyMessage())

    def get_attr_by_name(self):
        return self._connection.get_attr_by_name(cat_pb2.StringMessage(message='name'))

    def get_attr_by_stream(self):

        def stream_message():
            for s in ('name', 'age', 'love'):
                yield cat_pb2.StringMessage(message=s)

        response = self._connection.get_attr_by_name_with_stream(stream_message())

        return [x for x in response]

    def get_all(self):
        return self._connection.get_all(cat_pb2.EmptyMessage())


async def _rpc_client() -> None:

    _client = RpcClient()
    for name, response in (
        ('get_name', _client.get_name()),
        ('get_age', _client.get_age()),
        ('get_love', _client.get_love()),
        ('get_food', _client.get_food()),
        ('get_food', _client.get_attr_by_name()),
        ('get_all', _client.get_all()),
    ):
        result = await response
        if name == 'get_all':
            print(name, ' :=: ', json.loads(result.message.decode('utf-8')))
        else:
            print(name, ' :=: ', result.message)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(_rpc_client())




