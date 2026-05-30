from fastapi import APIRouter

from api.services.sales_service import (
    get_sales,
    get_late_arrivals
)

router = APIRouter()


@router.get("/sales")
def sales(limit: int = 100):

    return get_sales(
        limit
    ).to_dict(
        orient="records"
    )


@router.get("/late-arrivals")
def late_arrivals():

    return get_late_arrivals().to_dict(
        orient="records"
    )
