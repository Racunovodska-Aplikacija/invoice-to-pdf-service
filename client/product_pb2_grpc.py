# Generated-like gRPC module (handwritten to avoid grpc_tools dependency). DO NOT EDIT unless proto changes.
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from . import product_pb2 as product__pb2


class ProductServiceStub(object):
    """Product service definition"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProduct = channel.unary_unary(
            "/product.ProductService/GetProduct",
            request_serializer=product__pb2.GetProductRequest.SerializeToString,
            response_deserializer=product__pb2.GetProductResponse.FromString,
        )


class ProductServiceServicer(object):
    """Product service definition"""

    def GetProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetProduct": grpc.unary_unary_rpc_method_handler(
            servicer.GetProduct,
            request_deserializer=product__pb2.GetProductRequest.FromString,
            response_serializer=product__pb2.GetProductResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "product.ProductService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Product service definition"""

    @staticmethod
    def GetProduct(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/product.ProductService/GetProduct",
            product__pb2.GetProductRequest.SerializeToString,
            product__pb2.GetProductResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


