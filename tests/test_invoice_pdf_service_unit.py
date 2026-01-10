from __future__ import annotations

from unittest.mock import MagicMock
from uuid import uuid4


def test_generate_invoice_pdf_renders_template_and_returns_pdf(monkeypatch):
    import service.invoice_pdf_service as invoice_pdf_service_module

    mock_invoice_client = MagicMock()
    monkeypatch.setattr(invoice_pdf_service_module, "InvoiceClient", lambda: mock_invoice_client)

    class DummyHTML:
        def __init__(self, string: str, base_url: str | None = None):
            self.string = string
            self.base_url = base_url

        def write_pdf(self) -> bytes:
            return b"%PDF-1.4 fake"

    monkeypatch.setattr(invoice_pdf_service_module, "HTML", DummyHTML)

    svc = invoice_pdf_service_module.InvoicePdfService()
    mock_template = MagicMock()
    mock_template.render.return_value = "<html>ok</html>"
    svc.jinja.get_template = MagicMock(return_value=mock_template)

    invoice_id = uuid4()
    token = "jwt-token"

    dummy_invoice = MagicMock()
    dummy_invoice.invoice_number = "INV-1"
    dummy_invoice.model_dump.return_value = {"company": {"name": "ACME"}, "invoice_number": "INV-1", "lines": []}
    mock_invoice_client.get_invoice.return_value = dummy_invoice

    pdf_bytes, filename = svc.generate_invoice_pdf(invoice_id, token)

    assert pdf_bytes == b"%PDF-1.4 fake"
    assert filename == "invoice_INV-1.pdf"
    mock_invoice_client.get_invoice.assert_called_once_with(invoice_id, token)
    mock_template.render.assert_called_once_with(
        invoice={"company": {"name": "ACME"}, "invoice_number": "INV-1", "lines": []},
        company={"name": "ACME"},
    )

