import os

import grpc

from . import partner_pb2, partner_pb2_grpc


class PartnerClientError(Exception):
    pass


class PartnerClientNotFound(PartnerClientError):
    pass


class PartnerClient:
    def __init__(self):
        # Example: "localhost:50053" / "partner-service:50053"
        self.target = os.getenv("PARTNER_SERVICE_GRPC_TARGET", "localhost:50053")
        try:
            self.timeout_seconds = float(os.getenv("GRPC_TIMEOUT_SECONDS", "5"))
        except ValueError:
            self.timeout_seconds = 5.0

    def get_partner(self, partner_id: str):
        req = partner_pb2.GetPartnerRequest(id=partner_id)
        try:
            with grpc.insecure_channel(self.target) as channel:
                stub = partner_pb2_grpc.PartnerServiceStub(channel)
                return stub.GetPartner(req, timeout=self.timeout_seconds)
        except grpc.RpcError as e:
            code = e.code()
            if code == grpc.StatusCode.NOT_FOUND:
                raise PartnerClientNotFound() from e
            raise PartnerClientError(f"partner-service grpc error: {code}") from e


