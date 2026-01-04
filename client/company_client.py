import os

import grpc

from . import company_pb2, company_pb2_grpc


class CompanyClientError(Exception):
    pass


class CompanyClientNotFound(CompanyClientError):
    pass


class CompanyClient:
    def __init__(self):
        # Example: "localhost:50051" / "company-service:50051"
        self.target = os.getenv("COMPANY_SERVICE_GRPC_TARGET", "localhost:50051")
        try:
            self.timeout_seconds = float(os.getenv("GRPC_TIMEOUT_SECONDS", "5"))
        except ValueError:
            self.timeout_seconds = 5.0

    def get_company(self, company_id: str):
        req = company_pb2.GetCompanyRequest(id=company_id)
        try:
            with grpc.insecure_channel(self.target) as channel:
                stub = company_pb2_grpc.CompanyServiceStub(channel)
                return stub.GetCompany(req, timeout=self.timeout_seconds)
        except grpc.RpcError as e:
            code = e.code()
            if code == grpc.StatusCode.NOT_FOUND:
                raise CompanyClientNotFound() from e
            raise CompanyClientError(f"company-service grpc error: {code}") from e


