# Invoice to PDF Service

Invoice PDF generation service for the RAC application. Exposes a small REST API (FastAPI) that fetches invoice data from `invoice-service` and renders a PDF using Jinja2 + WeasyPrint.

## HTTP

- **Base Path**: `/invoice-pdf`
- **HTTP Port**: 8000
- **Docker Compose Host Port**: 8001 (maps `8001:8000`)

## REST API Endpoints

### PDF Generation (Protected)

#### Get Invoice PDF
```
GET /invoice-pdf/pdf/:invoiceId
```

**Auth:**
- `Authorization: Bearer {jwt-token}`
- or cookie: `jwt={jwt-token}`

**Response:**
- `Content-Type: application/pdf`
- `Content-Disposition: attachment; filename="invoice_<invoice_number>.pdf"`

### Health Check
```
GET /invoice-pdf/health
```

## Integrations

### invoice-service (HTTP)

The service calls invoice-service to retrieve the invoice data:
- `GET {INVOICE_SERVICE_URL}/invoices/{invoiceId}`

> Note: The PDF template expects enriched invoice data (company/partner/product details) to already be present in the invoice response.

## Environment Variables

- `INVOICE_SERVICE_URL` - Base URL of invoice-service (default: `http://localhost:8000`)
- `HTTP_TIMEOUT_SECONDS` - HTTP timeout for invoice-service requests (default: `5`)


## Running Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Tests

```bash
pytest
```

## Docker Build

```bash
docker build -t invoice-to-pdf-service:latest .
```