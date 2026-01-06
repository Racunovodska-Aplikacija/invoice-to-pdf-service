from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Dict, Any
from uuid import UUID

from pydantic import BaseModel


class InvoiceStatus(str, Enum):
    ISSUED = "ISSUED"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class InvoiceLineResponse(BaseModel):
    id: UUID
    invoice_id: UUID
    product_id: UUID
    amount: int
    product: Optional[Dict[str, Any]] = None  # gRPC product data


class InvoiceResponse(BaseModel):
    id: UUID
    user_id: UUID
    company_id: UUID
    partner_id: UUID
    invoice_number: str
    issue_date: datetime
    service_date: datetime
    due_date: datetime
    notes: Optional[str] = None
    status: InvoiceStatus
    lines: List[InvoiceLineResponse]
    company: Optional[Dict[str, Any]] = None  # gRPC company data
    partner: Optional[Dict[str, Any]] = None  # gRPC partner data


