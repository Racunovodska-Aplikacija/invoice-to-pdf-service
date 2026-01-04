# Generated-like gRPC module (handwritten to avoid grpc_tools dependency). DO NOT EDIT unless proto changes.
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from . import partner_pb2 as partner__pb2


class PartnerServiceStub(object):
    """Partner service definition"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPartner = channel.unary_unary(
            "/partner.PartnerService/GetPartner",
            request_serializer=partner__pb2.GetPartnerRequest.SerializeToString,
            response_deserializer=partner__pb2.GetPartnerResponse.FromString,
        )


class PartnerServiceServicer(object):
    """Partner service definition"""

    def GetPartner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PartnerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetPartner": grpc.unary_unary_rpc_method_handler(
            servicer.GetPartner,
            request_deserializer=partner__pb2.GetPartnerRequest.FromString,
            response_serializer=partner__pb2.GetPartnerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "partner.PartnerService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PartnerService(object):
    """Partner service definition"""

    @staticmethod
    def GetPartner(
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
            "/partner.PartnerService/GetPartner",
            partner__pb2.GetPartnerRequest.SerializeToString,
            partner__pb2.GetPartnerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


