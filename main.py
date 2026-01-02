from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Invoice to PDF Service",
    description="Microservice for generating PDF invoices",
    version="1.0.0",
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


