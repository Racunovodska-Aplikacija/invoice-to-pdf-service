from pathlib import Path
from uuid import UUID

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from client.invoice_client import InvoiceClient


class InvoicePdfService:
    def __init__(self):
        self.client = InvoiceClient()

        templates_dir = Path(__file__).resolve().parent.parent / "templates"
        self.jinja = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self._base_url = str(templates_dir)

    def generate_invoice_pdf(self, invoice_id: UUID) -> tuple[bytes, str]:
        invoice = self.client.get_invoice(invoice_id)
        template = self.jinja.get_template("invoice.html")
        html = template.render(invoice=invoice)

        pdf_bytes = HTML(string=html, base_url=self._base_url).write_pdf()
        filename = f"invoice_{invoice.invoice_number}.pdf"
        return pdf_bytes, filename


