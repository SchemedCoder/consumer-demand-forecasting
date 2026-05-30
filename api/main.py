from fastapi import FastAPI

from api.routers.sales import router as sales_router
from api.routers.products import router as products_router
from api.routers.health import router as health_router

app = FastAPI(
    title="Consumer Demand API",
    version="1.0.0"
)

app.include_router(
    health_router
)

app.include_router(
    sales_router
)

app.include_router(
    products_router
)
