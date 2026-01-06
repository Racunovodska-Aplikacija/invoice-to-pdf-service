from pathlib import Path
from uuid import UUID

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from client.invoice_client import InvoiceClient


class InvoicePdfService:
    def __init__(self):
        self.invoice_client = InvoiceClient()

        templates_dir = Path(__file__).resolve().parent.parent / "templates"
        self.jinja = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self._base_url = str(templates_dir)

    def generate_invoice_pdf(self, invoice_id: UUID, token: str) -> tuple[bytes, str]:
        # Get invoice with all enriched data from invoice service
        invoice = self.invoice_client.get_invoice(invoice_id, token)
        
        # Convert to dict for template rendering
        invoice_ctx = invoice.model_dump()
        
        # Company and partner data are already included from gRPC
        company = invoice_ctx.get('company')
        
        # Product data is already included in each line
        # No need to fetch separately

        template = self.jinja.get_template("invoice.html")
        html = template.render(invoice=invoice_ctx, company=company)

        pdf_bytes = HTML(string=html, base_url=self._base_url).write_pdf()
        filename = f"invoice_{invoice.invoice_number}.pdf"
        return pdf_bytes, filename


