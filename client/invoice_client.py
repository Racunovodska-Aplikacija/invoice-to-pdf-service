import os
from uuid import UUID

import requests

from models.schemas import InvoiceResponse


class InvoiceClientError(Exception):
    pass


class InvoiceClientNotFound(InvoiceClientError):
    pass


class InvoiceClient:
    def __init__(self):
        self.base_url = os.getenv("INVOICE_SERVICE_URL", "http://localhost:8000").rstrip("/")
        try:
            self.timeout_seconds = float(os.getenv("HTTP_TIMEOUT_SECONDS", "5"))
        except ValueError:
            self.timeout_seconds = 5.0

    def get_invoice(self, invoice_id: UUID) -> InvoiceResponse:
        url = f"{self.base_url}/invoices/{invoice_id}"
        try:
            resp = requests.get(url, timeout=self.timeout_seconds)
        except requests.RequestException as e:
            raise InvoiceClientError(str(e)) from e

        if resp.status_code == 404:
            raise InvoiceClientNotFound()
        if resp.status_code >= 400:
            raise InvoiceClientError(f"invoice-service error: {resp.status_code}")

        try:
            data = resp.json()
        except ValueError as e:
            raise InvoiceClientError("invalid JSON from invoice-service") from e

        return InvoiceResponse.model_validate(data)


