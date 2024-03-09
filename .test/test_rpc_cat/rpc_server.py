# coding: utf-8
import asyncio
import json
import logging

import grpc

import proto.rpc_cat_pb2 as rpc_cat_pb2
import proto.rpc_cat_pb2_grpc as rpc_cat_pb2_grpc
from cat import Cat


class RpcCatServer(rpc_cat_pb2_grpc.RpcCatServicer):
    _cat: Cat = Cat()

    def get_name(self, request, context):
        return rpc_cat_pb2.StringMessage(message=self._cat.name())

    def get_age(self, request, context):
        return rpc_cat_pb2.IntMessage(message=self._cat.age())

    def get_love(self, request, context):
        return rpc_cat_pb2.TupleMessage(message=self._cat.love())

    def get_food_once(self, request, context):
        return rpc_cat_pb2.FoodMessage(message=self._cat.eat_food_once())

    def get_attr_by_name(self, request: rpc_cat_pb2.StringMessage, context):
        return rpc_cat_pb2.StringMessage(message=self._cat.get_attr_by_name(request.message))

    def get_attr_by_name_with_stream(self, request_iterator, context):
        for request in request_iterator:
            yield rpc_cat_pb2.StringMessage(message=self._cat.get_attr_by_name(request.message))

    def get_all(self, request, context):
        msg = json.dumps(self._cat.all_attr()).encode('utf-8')
        # msg.update(self._cat.all_attr())
        return rpc_cat_pb2.AllMessage(message=msg)


async def _server() -> None:
    server = grpc.aio.server()
    rpc_cat_pb2_grpc.add_RpcCatServicer_to_server(RpcCatServer(), server)
    listen_addr = '[::]:50052'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(_server())
