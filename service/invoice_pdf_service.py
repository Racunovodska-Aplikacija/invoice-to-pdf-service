from pathlib import Path
from uuid import UUID

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML

from client.company_client import CompanyClient
from client.invoice_client import InvoiceClient
from client.product_client import ProductClient, ProductClientNotFound
from client.partner_client import PartnerClient, PartnerClientNotFound


class InvoicePdfService:
    def __init__(self):
        self.invoice_client = InvoiceClient()
        self.company_client = CompanyClient()
        self.product_client = ProductClient()
        self.partner_client = PartnerClient()

        templates_dir = Path(__file__).resolve().parent.parent / "templates"
        self.jinja = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )
        self._base_url = str(templates_dir)

    def generate_invoice_pdf(self, invoice_id: UUID) -> tuple[bytes, str]:
        invoice = self.invoice_client.get_invoice(invoice_id)
        company = self.company_client.get_company(str(invoice.company_id))

        # Enrich each invoice line with product data (available in template as line.product.*)
        invoice_ctx = invoice.model_dump()
        for line_ctx, line in zip(invoice_ctx.get("lines", []), invoice.lines):
            try:
                product = self.product_client.get_product(str(line.product_id))
            except ProductClientNotFound:
                product = None
            line_ctx["product"] = product

        # Fetch partner data (available in template as invoice.partner.*)
        try:
            partner = self.partner_client.get_partner(str(invoice.partner_id))
        except PartnerClientNotFound:
            partner = None
        invoice_ctx["partner"] = partner

        template = self.jinja.get_template("invoice.html")
        html = template.render(invoice=invoice_ctx, company=company)

        pdf_bytes = HTML(string=html, base_url=self._base_url).write_pdf()
        filename = f"invoice_{invoice.invoice_number}.pdf"
        return pdf_bytes, filename


