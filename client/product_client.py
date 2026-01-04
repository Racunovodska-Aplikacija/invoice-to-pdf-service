import os

import grpc

from . import product_pb2, product_pb2_grpc


class ProductClientError(Exception):
    pass


class ProductClientNotFound(ProductClientError):
    pass


class ProductClient:
    def __init__(self):
        # Example: "localhost:50052" / "product-service:50052"
        self.target = os.getenv("PRODUCT_SERVICE_GRPC_TARGET", "localhost:50052")
        try:
            self.timeout_seconds = float(os.getenv("GRPC_TIMEOUT_SECONDS", "5"))
        except ValueError:
            self.timeout_seconds = 5.0

    def get_product(self, product_id: str):
        req = product_pb2.GetProductRequest(id=product_id)
        try:
            with grpc.insecure_channel(self.target) as channel:
                stub = product_pb2_grpc.ProductServiceStub(channel)
                return stub.GetProduct(req, timeout=self.timeout_seconds)
        except grpc.RpcError as e:
            code = e.code()
            if code == grpc.StatusCode.NOT_FOUND:
                raise ProductClientNotFound() from e
            raise ProductClientError(f"product-service grpc error: {code}") from e


