from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import Response

from client.invoice_client import InvoiceClientNotFound, InvoiceClientError
from service.invoice_pdf_service import InvoicePdfService

router = APIRouter(prefix="/pdf", tags=["pdf"])


def get_service() -> InvoicePdfService:
    return InvoicePdfService()


@router.get("/{invoice_id}")
def get_invoice_pdf(invoice_id: UUID, request: Request, service: InvoicePdfService = Depends(get_service)):
    # Extract JWT token from request
    token = None
    auth_header = request.headers.get("authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header[7:]
    elif "jwt" in request.cookies:
        token = request.cookies["jwt"]
    
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized - No token provided")
    
    try:
        pdf_bytes, filename = service.generate_invoice_pdf(invoice_id, token)
    except InvoiceClientNotFound as e:
        print(f"Invoice not found: {invoice_id} - {e}")
        raise HTTPException(status_code=404, detail="Invoice not found")
    except InvoiceClientError as e:
        print(f"Failed to fetch invoice {invoice_id}: {e}")
        raise HTTPException(status_code=502, detail=f"Failed to fetch invoice from invoice-service: {str(e)}")
    except Exception as e:
        print(f"Error generating PDF for invoice {invoice_id}: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to generate PDF: {str(e)}")
 
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


