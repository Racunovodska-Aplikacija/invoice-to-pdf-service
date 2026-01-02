from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class InvoiceStatus(str, Enum):
    ISSUED = "ISSUED"
    PAID = "PAID"
    CANCELLED = "CANCELLED"


class InvoiceLineResponse(BaseModel):
    id: UUID
    invoice_id: UUID
    description: str
    quantity: int
    unit_price: Decimal
    line_total: Decimal


class InvoiceResponse(BaseModel):
    id: UUID
    invoice_number: str
    customer_id: UUID
    issue_date: datetime
    due_date: datetime
    status: InvoiceStatus
    subtotal: Decimal
    tax_total: Decimal
    total: Decimal
    created_at: datetime
    lines: List[InvoiceLineResponse]


