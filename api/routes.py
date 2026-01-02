from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

from client.invoice_client import InvoiceClientNotFound, InvoiceClientError
from service.invoice_pdf_service import InvoicePdfService

router = APIRouter(prefix="/pdf", tags=["pdf"])


def get_service() -> InvoicePdfService:
    return InvoicePdfService()


@router.get("/{invoice_id}")
def get_invoice_pdf(invoice_id: UUID, service: InvoicePdfService = Depends(get_service)):
    # try:
    #     pdf_bytes, filename = service.generate_invoice_pdf(invoice_id)
    # except InvoiceClientNotFound:
    #     raise HTTPException(status_code=404, detail="Invoice not found")
    # except InvoiceClientError:
    #     raise HTTPException(status_code=502, detail="Failed to fetch invoice from invoice-service")
    # except Exception:
    #     raise HTTPException(status_code=500, detail="Failed to generate PDF")
    pdf_bytes, filename = service.generate_invoice_pdf(invoice_id)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


